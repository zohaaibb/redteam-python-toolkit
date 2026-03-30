import base64
import sys

def encode_string(text):
    """Encode a string to base64"""
    try:
        encoded = base64.b64encode(text.encode()).decode()
        return encoded, None
    except Exception as e:
        return None, str(e)

def decode_string(encoded_text):
    """Decode a base64 string"""
    try:
        decoded = base64.b64decode(encoded_text).decode()
        return decoded, None
    except Exception as e:
        return None, str(e)

def main():
    print("=" * 50)
    print("Base64 Encoder/Decoder Tool")
    print("=" * 50)
    print("1. Encode string")
    print("2. Decode string")
    print("3. Exit")
    
    while True:
        print("\n" + "-" * 30)
        choice = input("Choose option (1/2/3): ").strip()
        
        if choice == '1':
            text = input("Enter text to encode: ")
            encoded, error = encode_string(text)
            if encoded:
                print(f"\n[+] Encoded:\n{encoded}\n")
                print(f"[+] Bytes form: {encoded.encode()}")
            else:
                print(f"[-] Error: {error}")
                
        elif choice == '2':
            b64_text = input("Enter base64 to decode: ")
            decoded, error = decode_string(b64_text)
            if decoded:
                print(f"\n[+] Decoded:\n{decoded}")
            else:
                print(f"[-] Error: {error}")
                
        elif choice == '3':
            print("[*] Goodbye!")
            break
        else:
            print("[-] Invalid choice")

if __name__ == "__main__":
    main()
