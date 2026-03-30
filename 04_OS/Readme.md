# Day 04: os Module — File Operations

## What I Learned
- **os.getcwd()** — get current directory
- **os.listdir()** — list files in directory
- **os.path.join()** — build paths safely (cross-platform)
- **os.path.exists()** / **os.path.isfile()** / **os.path.isdir()** — check what exists
- **os.walk()** — traverse directory trees
- **os.stat()** — get file metadata (size, timestamps, permissions)
- **os.access()** — check read/write permissions
- **os.makedirs()** — create directories
- **os.remove()** / **os.rmdir()** — delete files/directories

## Script: directory_scanner.py
Scans directories for interesting files (configs, keys, passwords, etc.)

Features:
- Pattern matching on filenames
- Extension filtering
- Depth limiting (avoid going too deep)
- Permission checking
- Saves results to timestamped file

## What I Modified
- Changed extensions to find `.log` files
- Added file creation time to output
- Changed max depth to 1 for shallow scans

## Red Team Application
- Post-exploitation recon: find credentials, configs, keys
- Automate discovery of sensitive files
- Check permissions for privilege escalation paths
- Build reports of interesting findings

## Next
Day 05: base64 — Encoding payloads for evasion
