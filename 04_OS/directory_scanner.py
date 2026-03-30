import os
import sys
from datetime import datetime

# Patterns to look for in filenames
INTERESTING_PATTERNS = [
    "passwd",
    "shadow", 
    "config",
    "secret",
    "key",
    "password",
    "credential",
    ".env",
    "id_rsa",
    "id_ecdsa"
]

# Extensions to look for
INTERESTING_EXTENSIONS = [
    ".conf",
    ".config", 
    ".ini",
    ".yaml",
    ".yml",
    ".json",
    ".xml",
    ".env",
    ".pem",
    ".key",
    ".crt",
    ".sql",
    ".db"
]

def find_files(start_path, max_depth=3):
    """Find interesting files in directory tree"""
    found = []
    current_depth = start_path.count(os.sep)
    
    try:
        for root, dirs, files in os.walk(start_path):
            # Check depth
            depth = root.count(os.sep) - current_depth
            if depth > max_depth:
                del dirs[:]  # Don't go deeper
                continue
            
            for file in files:
                file_lower = file.lower()
                full_path = os.path.join(root, file)
                
                # Check filename patterns
                for pattern in INTERESTING_PATTERNS:
                    if pattern in file_lower:
                        found.append(full_path)
                        break
                else:
                    # Check extensions
                    for ext in INTERESTING_EXTENSIONS:
                        if file_lower.endswith(ext):
                            found.append(full_path)
                            break
                            
    except PermissionError:
        print(f"[-] Permission denied: {start_path}")
    except Exception as e:
        print(f"[-] Error: {e}")
    
    return found

def get_file_info(filepath):
    """Get file size and permissions"""
    try:
        stat = os.stat(filepath)
        size = stat.st_size
        size_kb = round(size / 1024, 2)
        
        # Check permissions
        readable = os.access(filepath, os.R_OK)
        writable = os.access(filepath, os.W_OK)
        
        return {
            "path": filepath,
            "size_kb": size_kb,
            "readable": readable,
            "writable": writable
        }
    except Exception as e:
        return {"path": filepath, "error": str(e)}

def save_results(results, filename):
    """Save results to file"""
    try:
        with open(filename, 'w') as f:
            f.write("=== Directory Scan Results ===\n")
            f.write(f"Scan date: {datetime.now()}\n")
            f.write(f"Files found: {len(results)}\n\n")
            
            for r in results:
                f.write(f"File: {r['path']}\n")
                if 'error' in r:
                    f.write(f"  Error: {r['error']}\n")
                else:
                    f.write(f"  Size: {r['size_kb']} KB\n")
                    f.write(f"  Readable: {r['readable']}\n")
                    f.write(f"  Writable: {r['writable']}\n")
                f.write("-" * 40 + "\n")
        
        print(f"[+] Saved to: {filename}")
    except Exception as e:
        print(f"[-] Failed to save: {e}")

def main():
    print("=" * 50)
    print("Directory Scanner")
    print("=" * 50)
    
    # Get target directory
    target = input("Enter directory to scan (default: current): ").strip()
    if not target:
        target = os.getcwd()
    
    # Check if directory exists
    if not os.path.exists(target):
        print(f"[-] Directory does not exist: {target}")
        return
    
    if not os.path.isdir(target):
        print(f"[-] Not a directory: {target}")
        return
    
    print(f"\n[*] Scanning: {target}")
    print(f"[*] Current directory: {os.getcwd()}")
    
    # Get depth
    depth_input = input("Enter max depth (default 3): ").strip()
    if depth_input.isdigit():
        max_depth = int(depth_input)
    else:
        max_depth = 3
    
    print("\n[*] Searching for interesting files...\n")
    
    # Find files
    files = find_files(target, max_depth)
    
    if not files:
        print("[-] No interesting files found")
        return
    
    print(f"[+] Found {len(files)} interesting files:\n")
    
    # Get info for each file
    results = []
    for i, f in enumerate(files, 1):
        print(f"[{i}] Processing: {f}")
        info = get_file_info(f)
        results.append(info)
        
        if 'error' not in info:
            print(f"    Size: {info['size_kb']} KB | Readable: {info['readable']}")
    
    # Save results
    save_choice = input("\nSave results to file? (y/n): ").strip().lower()
    if save_choice == 'y':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"scan_{timestamp}.txt"
        save_results(results, filename)
    
    print("\n[*] Done.")

if __name__ == "__main__":
    main()
