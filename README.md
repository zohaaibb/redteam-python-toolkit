# 🔥 REDTEAM-PYTHON-TOOLKIT

### *Because courses teach theory. Building teaches everything else.*

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Purpose](https://img.shields.io/badge/Purpose-Red%20Team-red)
![License](https://img.shields.io/badge/License-Educational%20Only-orange)

---

## 🎯 What Is This?

A growing collection of Python scripts for **red team operations, penetration testing, and security automation**.

Every script here is:
- ✅ **Actually written** (not copy-pasted without understanding)
- ✅ **Heavily commented** so you know what each line does
- ✅ **Tested and working**
- ✅ **Designed to be modified** - break them, fix them, make them yours

This isn't a "course project." This is **daily work** - one script at a time, until I own this shit.

---

## 🚀 Why This Exists

I got tired of:
- Tutorials that teach theory but not application
- Courses that take months but leave you unable to build
- "Learn Python" guides that have nothing to do with red teaming

So I'm building my own toolkit. **Publicly. Every day.**

If you're on the same path, steal everything here. Then build your own.

---

## 📂 The Arsenal

| Category | Libraries | What's Inside |
|----------|-----------|---------------|
| **Core Networking** | `socket` | Port scanners, banner grabbers, reverse shells |
| **Web Tools** | `requests` | Website checkers, dir bruteforce, file downloaders |
| **System Access** | `subprocess`, `os` | Nmap wrappers, command executors, file ops |
| **Encoding & Obfuscation** | `base64`, `cryptography` | Payload encoders/decoders, XOR obfuscation |
| **Red Team Specific** | `paramiko`, `scapy`, `ctypes` | SSH attacks, packet crafting, Windows API |
| **Speed & Scale** | `threading` | Fast scanners, parallel bruteforce |
| **Reconnaissance** | *Combined* | Network scans, subdomain finders, SSL checkers |
| **Initial Access** | *Combined* | Phishing page cloners, payload generators |
| **Post-Exploitation** | *Combined* | File downloaders, persistence mechanisms |
| **Evasion** | *Combined* | Obfuscators, sandbox detectors, encrypted C2 |

*Each folder contains its own README explaining the scripts inside.*

---

## 🔧 Setup

```bash
# Clone this toolkit
git clone https://github.com/[YOUR_USERNAME]/redteam-python-toolkit.git
cd redteam-python-toolkit

# Install dependencies
pip install -r requirements.txt

# Pick a script and run it
python 01_socket/port_scanner.py
