import base64

# Simple payload encoding example
command = "whoami"

# Encode: string → bytes → base64
encoded = base64.b64encode(command.encode())

print("=== Basic Payload Encoding ===")
print(f"Original: {command}")
print(f"Encoded (bytes): {encoded}")
print(f"Encoded (string): {encoded.decode()}")

# Decode: base64 → bytes → string
decoded = base64.b64decode(encoded).decode()
print(f"Decoded: {decoded}")
