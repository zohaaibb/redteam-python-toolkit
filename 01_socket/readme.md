# 🔌 Socket Programming

*Because everything in red teaming starts with a connection.*

## What I Learned Here

Socket programming is the foundation of network communication. Every connection you make - whether scanning, exploiting, or exfiltrating - uses sockets under the hood.

### Core Concepts

| Concept | What It Means | Why It Matters |
|---------|---------------|----------------|
| **Socket** | Endpoint for network communication | Everything network-related uses sockets |
| **AF_INET** | IPv4 address family | Tells Python to use IPv4 |
| **SOCK_STREAM** | TCP protocol | Reliable connections (vs UDP) |
| **connect()** | Establishes connection | Tries to connect to target |
| **connect_ex()** | Connect with return code | Returns 0 if open, error code if closed |
| **settimeout()** | Max wait time | Prevents hanging on dead ports |
| **Port** | Door into a computer | 22=SSH, 80=HTTP, 443=HTTPS |

---

## Scripts in This Folder

### 1. `port_scanner.py` - Basic
Checks if specific ports are open on a target.

**What I learned:**
- Creating sockets
- Looping through ports
- Handling connection results
- Why timeouts matter

### 2. `banner_grabber.py` - Medium
Connects to open ports and grabs service banners.

**What I learned:**
- Receiving data after connection
- Service fingerprinting
- How banners reveal versions

### 3. `reverse_shell.py` - Advanced
Creates a listener that gives shell access when connected.

**What I learned:**
- Binding sockets (server mode)
- Accepting connections
- Handling multiple connections
- Real shell interaction

---

## The "Break It" Method

For each script, I did this:

| Change | What Broke | What I Learned |
|--------|------------|----------------|
| Removed `settimeout()` | Script hung on closed ports | Timeout prevents hanging |
| Changed to `connect()` | Script crashed on closed ports | `connect_ex` returns codes, `connect` throws errors |
| Changed `AF_INET` to `AF_INET6` | Couldn't connect to IPv4 | Address families must match |
| Removed `if result == 0:` | Printed all ports as open | Filtering is essential |
| Empty port list | Nothing happened | Loops need data |

---

## Questions I Can Now Answer

- [x] What's the difference between TCP and UDP?
- [x] Why use `connect_ex()` instead of `connect()`?
- [x] What happens if timeout is too short/too long?
- [x] How would I scan all 65535 ports? (and why that's dumb)
- [x] How would a defender detect this scan?

---

## Red Team Application

These scripts are the building blocks for:
- Reconnaissance (what's open?)
- Enumeration (what's running?)
- Initial access (can I connect?)
- C2 (reverse shells)

Every tool like nmap, netcat, or Metasploit is just these concepts wrapped in more features.

---

## Next Steps

Day 02: `02_requests/` - Web attacks with Python

---

*Built by breaking things until I understood them.*
