# Day 05: base64 — Encoding Payloads

## What I Learned
- **base64.b64encode()** — encode strings/bytes to base64
- **base64.b64decode()** — decode base64 back to original
- **.encode() / .decode()** — convert between strings and bytes
- Base64 is obfuscation, not encryption (defenders can decode instantly)

## Scripts
| Script | Purpose |
|--------|---------|
| `encode_payload.py` | Basic encode/decode example |
| `payload_encoder.py` | Encode reverse shell commands |
| `encoder_tool.py` | Interactive encoder/decoder |
| `file_encoder.py` | Encode/decode entire files |

## Key Code Pattern
```python
import base64

# Encode
encoded = base64.b64encode(command.encode()).decode()

# Decode
decoded = base64.b64decode(encoded).decode()
```
## Red Team Application

->Hide reverse shell commands from plain text detection

->Transfer binary files through text-only channels

->Obfuscate C2 communication

->Bypass simple string-based detection rules

## Limitations

->Base64 alone is NOT encryption. A defender can decode it instantly. Real evasion requires:

->Base64 + XOR

->AES encryption

->Custom encoding

->Packing/compression

### Next

Day 06: paramiko — SSH attacks and lateral movement
