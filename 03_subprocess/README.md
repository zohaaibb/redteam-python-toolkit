# Day 03: subprocess — System Commands

## Scripts
- `nmap_wrapper.py` - Python wrapper for nmap scans

## What I Learned
- **subprocess.run()**: Run system commands from Python
- **capture_output**: Capture stdout/stderr instead of printing
- **text=True**: Return strings instead of bytes
- **timeout**: Prevent hanging on slow commands
- **returncode**: 0 = success, non-zero = error
- **Exception handling**: TimeoutExpired, FileNotFoundError, etc.
- **Security**: Using lists (safe) vs shell=True (dangerous)

## What I Broke
| Change | Result | Lesson |
|--------|--------|--------|
| Removed timeout | Script hung forever | Always set timeouts |
| Removed try/except | Script crashed on error | Error handling is essential |
| Used string with shell=True | Security risk | Lists are safer |
| Entered invalid target | nmap failed, caught by except | Check return codes |

## Red Team Application
- Automate network scans across multiple targets
- Parse nmap output for interesting services
- Chain scans together (nmap → grep → attack)
- Generate timestamped scan reports automatically

## Next
Day 04: os module — File operations and system paths
