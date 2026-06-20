# SSH Credential Testing Tool

**Date:** June 20, 2026
**Language:** Python 3
**Library Used:** Paramiko

---

# Overview

The SSH Credential Testing Tool is a Python-based utility designed to perform authorized SSH login testing against a target system using a username and a password wordlist.

The tool attempts authentication using each password from the supplied wordlist and reports successful credentials when found.

This project was developed as part of Python security automation practice and demonstrates:

* SSH authentication using Paramiko
* File handling
* Error handling
* Command-line arguments
* Security assessment automation
* Credential validation workflows

> **Important:** Use this tool only on systems you own or have explicit authorization to test.

---

# Features

* SSH authentication testing using Paramiko
* Custom username support
* Custom SSH port support
* Password wordlist support
* Automatic success detection
* Graceful handling of authentication failures
* Connection timeout protection
* Clear progress output

---

# Requirements

## Python Version

* Python 3.x

## Required Library

Install Paramiko:

```bash
pip install paramiko
```

Verify installation:

```bash
python3 -c "import paramiko; print(paramiko.__version__)"
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ssh-credential-tester.git
cd ssh-credential-tester
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install paramiko
```

---

# Usage

## Basic Syntax

```bash
python3 ssh_bruteforce.py <target> <username> <wordlist> [port]
```

---

## Examples

### Default SSH Port (22)

```bash
python3 ssh_bruteforce.py 192.168.1.10 admin passwords.txt
```

### Custom SSH Port

```bash
python3 ssh_bruteforce.py 192.168.1.10 admin passwords.txt 2222
```

---

# Parameters

| Parameter | Description                     |
| --------- | ------------------------------- |
| target    | Target IP address or hostname   |
| username  | Username to test                |
| wordlist  | Path to password wordlist       |
| port      | Optional SSH port (default: 22) |

---

# Sample Output

```text
[*] Loaded 500 password(s) from passwords.txt
[*] Target: 192.168.1.10:22
[*] Username: admin

[*] Attempt 1/500: password
[*] Attempt 2/500: admin123
[*] Attempt 3/500: letmein

[+] Password found: SuperSecurePassword

[*] Valid credentials: admin:SuperSecurePassword
[*] Connect with: ssh admin@192.168.1.10
```

---

# How It Works

1. Loads passwords from a supplied wordlist.
2. Establishes an SSH connection using Paramiko.
3. Attempts authentication using the specified username.
4. Detects successful logins.
5. Stops execution upon finding valid credentials.
6. Reports the discovered password.

---

# Project Structure

```text
ssh-credential-tester/
│
├── ssh_bruteforce.py
├── requirements.txt
├── README.md
└── wordlists/
    └── passwords.txt
```

---

# Wordlists

For testing in lab environments, publicly available wordlists can be downloaded from open-source security resources such as:

* SecLists
* PayloadsAllTheThings
* Kali Linux wordlists

Example:

```bash
git clone https://github.com/danielmiessler/SecLists.git
```

Common wordlist:

```text
SecLists/Passwords/Common-Credentials/
```

---

# Security Notes

* Only use against systems you own or are authorized to assess.
* Unauthorized password testing may violate laws and organizational policies.
* Large wordlists can generate significant authentication traffic and may trigger security monitoring systems.
* Consider rate limits and account lockout policies during assessments.

---

# Learning Objectives

This project demonstrates:

* Python networking
* SSH automation
* Paramiko usage
* File I/O
* Exception handling
* Security scripting fundamentals
* Authentication testing concepts

---

# Future Improvements

Potential enhancements include:

* Multi-threaded execution
* Username wordlist support
* Logging to file
* Result export (CSV/JSON)
* Banner grabbing
* Proxy support
* Retry/backoff mechanisms
* Progress bar integration

---

# Disclaimer

This tool is intended for educational purposes, security research, and authorized penetration testing only.

Users are responsible for complying with all applicable laws, regulations, and organizational policies.

The author assumes no responsibility for misuse or damage caused by this software.
