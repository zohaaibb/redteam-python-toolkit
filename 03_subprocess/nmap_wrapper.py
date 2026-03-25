import subprocess
from datetime import datetime

def run_nmap_scan(target, ports="1-1000", flags="-sV"):
    """Run nmap scan and return results."""
    command = ["nmap", flags, "-p", ports, target]
    print(f"[*] Running: {' '.join(command)}")
    
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            return {
                "success": True,
                "output": result.stdout,
                "error": None
            }
        else:
            return {
                "success": False,
                "output": result.stdout,
                "error": result.stderr
            }
            
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": None,
            "error": "Scan timed out after 5 minutes"
        }
    except FileNotFoundError:
        return {
            "success": False,
            "output": None,
            "error": "nmap not installed or not in PATH"
        }
    except Exception as e:
        return {
            "success": False,
            "output": None,
            "error": str(e)
        }

def save_results(target, output):
    """Save scan results to file with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"nmap_scan_{target}_{timestamp}.txt"
    
    try:
        with open(filename, "w") as f:
            f.write(f"=== Nmap Scan Report ===\n")
            f.write(f"Target: {target}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*50 + "\n\n")
            f.write(output)
        
        print(f"[+] Results saved to: {filename}")
        return filename
    except Exception as e:
        print(f"[!] Failed to save: {e}")
        return None

def main():
    print("="*50)
    print("Python Nmap Wrapper")
    print("="*50)
    
    target = input("Enter target IP or hostname: ").strip()
    if not target:
        print("[!] No target entered")
        return
    
    ports = input("Enter ports (default 1-1000): ").strip()
    if not ports:
        ports = "1-1000"
    
    flags = input("Enter nmap flags (default -sV): ").strip()
    if not flags:
        flags = "-sV"
    
    print("\n[*] Starting scan...\n")
    
    result = run_nmap_scan(target, ports, flags)
    
    if result["success"]:
        print("\n[+] SCAN COMPLETE")
        print("="*50)
        print(result["output"])
        
        save = input("\nSave results to file? (y/n): ").strip().lower()
        if save == 'y':
            save_results(target, result["output"])
    else:
        print(f"\n[!] Scan failed: {result['error']}")
    
    print("\n[*] Done.")

if __name__ == "__main__":
    main()
