import base64
import os

def encode_file_to_base64(input_file, output_file=None):
    """
    Encode a file to base64
    
    Args:
        input_file: Path to file to encode
        output_file: Optional path to save encoded output
    
    Returns:
        Encoded string or None if error
    """
    try:
        # Check if file exists
        if not os.path.exists(input_file):
            print(f"[-] File not found: {input_file}")
            return None
        
        # Get file size
        file_size = os.path.getsize(input_file)
        print(f"[*] Encoding file: {input_file} ({file_size} bytes)")
        
        # Read file as bytes
        with open(input_file, 'rb') as f:
            file_bytes = f.read()
        
        # Encode to base64
        encoded = base64.b64encode(file_bytes)
        
        # Save or display
        if output_file:
            with open(output_file, 'w') as f:
                f.write(encoded.decode())
            print(f"[+] Encoded file saved to: {output_file}")
        else:
            # Show preview
            preview = encoded.decode()[:100]
            print(f"[+] Encoded (preview): {preview}...")
            print(f"[+] Total length: {len(encoded)} characters")
        
        return encoded
        
    except Exception as e:
        print(f"[-] Error encoding file: {e}")
        return None

def decode_base64_to_file(encoded_file, output_file):
    """
    Decode base64 file to original
    
    Args:
        encoded_file: Path to base64 encoded file
        output_file: Path to save decoded file
    """
    try:
        # Check if file exists
        if not os.path.exists(encoded_file):
            print(f"[-] File not found: {encoded_file}")
            return False
        
        # Read encoded content
        with open(encoded_file, 'r') as f:
            encoded_content = f.read()
        
        print(f"[*] Decoding file: {encoded_file} ({len(encoded_content)} chars)")
        
        # Decode from base64
        decoded = base64.b64decode(encoded_content)
        
        # Save to output file
        with open(output_file, 'wb') as f:
            f.write(decoded)
        
        print(f"[+] Decoded file saved to: {output_file}")
        return True
        
    except Exception as e:
        print(f"[-] Error decoding file: {e}")
        return False

def main():
    print("=" * 50)
    print("File Base64 Encoder/Decoder")
    print("=" * 50)
    print("1. Encode file to base64")
    print("2. Decode base64 file to original")
    print("3. Exit")
    
    while True:
        print("\n" + "-" * 30)
        choice = input("Choose option (1/2/3): ").strip()
        
        if choice == '1':
            input_file = input("File to encode: ").strip()
            output_file = input("Output file (optional, press Enter for preview): ").strip()
            
            if output_file:
                encode_file_to_base64(input_file, output_file)
            else:
                encode_file_to_base64(input_file)
                
        elif choice == '2':
            encoded_file = input("Encoded file: ").strip()
            output_file = input("Output file name: ").strip()
            decode_base64_to_file(encoded_file, output_file)
            
        elif choice == '3':
            print("[*] Goodbye!")
            break
        else:
            print("[-] Invalid choice")

if __name__ == "__main__":
    main()
