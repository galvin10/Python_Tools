# TCP Port Scanner

**Author:** [Your Name]
**Date:** 20 June 2026
**Category:** Python for Pentesters / Network Reconnaissance

---

## Overview

The TCP Port Scanner is a Python-based reconnaissance tool designed to identify open TCP ports on a target host. It performs TCP connect scans using Python's built-in `socket` library and provides basic service identification for commonly used ports.

This project was developed as part of my cybersecurity and red team learning journey to gain a deeper understanding of network enumeration, socket programming, and reconnaissance techniques.

---

## Features

* Hostname and IP address support
* TCP Connect Scan using `connect_ex()`
* Configurable port range
* Common service identification
* Error handling for unreachable hosts
* Fast and lightweight implementation
* Command-line interface

---

## Technologies Used

* Python 3
* Socket Programming
* Networking Fundamentals
* TCP/IP Protocol Suite

---

## How It Works

### 1. Target Resolution

The scanner first attempts to resolve a hostname into an IP address using:

```python
socket.gethostbyname()
```

Example:

```bash
python3 port_scanner.py example.com
```

Output:

```text
[*] Resolved example.com to 93.184.216.34
```

---

### 2. TCP Port Probing

For each port in the specified range, the scanner:

1. Creates a TCP socket.
2. Attempts a connection using `connect_ex()`.
3. Determines whether the port is open based on the return value.

Example:

```python
result = sock.connect_ex((ip, port))
```

A return value of:

```text
0 = Port Open
Other Values = Port Closed
```

---

### 3. Service Mapping

The scanner maps common ports to their likely services.

Examples:

| Port | Service |
| ---- | ------- |
| 21   | FTP     |
| 22   | SSH     |
| 80   | HTTP    |
| 443  | HTTPS   |
| 445  | SMB     |
| 3389 | RDP     |
| 3306 | MySQL   |

---

## Usage

### Scan Default Ports (1-1024)

```bash
python3 port_scanner.py 192.168.1.10
```

### Scan Custom Port Range

```bash
python3 port_scanner.py 192.168.1.10 5000
```

### Scan Hostname

```bash
python3 port_scanner.py scanme.nmap.org 1024
```

---

## Example Output

```text
[*] Scanning 192.168.1.10 (ports 1-1024)...

[+] Port 22 is open
[+] Port 80 is open
[+] Port 443 is open

[*] Scan complete. 3 open port(s) found:

Port      Likely Service
------------------------------
22        SSH
80        HTTP
443       HTTPS
```

---

## Security Use Cases

This tool can be used during:

### Reconnaissance

Identify exposed services running on a target host.

### Attack Surface Mapping

Discover services that may contain vulnerabilities.

### Internal Network Assessments

Quickly enumerate accessible hosts and services.

### Red Team Operations

Perform initial service discovery before enumeration and exploitation.

---

## Learning Objectives

Through this project, I gained hands-on experience with:

* Python socket programming
* TCP connection handling
* Port scanning methodology
* Hostname resolution
* Network reconnaissance techniques
* Command-line tool development
* Error handling and exception management

---

## Future Improvements

Planned enhancements include:

### Multi-threading

Increase scanning speed using:

```python
concurrent.futures.ThreadPoolExecutor
```

### Banner Grabbing

Retrieve service banners from open ports.

Example:

```text
Apache/2.4.57
OpenSSH_9.3
```

### Output Files

Save scan results to:

```text
results.txt
results.csv
```

### Full Service Detection

Use:

```python
socket.getservbyport()
```

for dynamic service identification.

### Scan Profiles

Implement modes similar to Nmap:

```bash
--top100
--top1000
--full
```

---

## Ethical Use

This tool is intended solely for:

* Educational purposes
* Personal lab environments
* Authorized penetration testing
* Security research

Always obtain proper authorization before scanning systems that you do not own or manage.

---

## Conclusion

This TCP Port Scanner project strengthened my understanding of network reconnaissance and socket programming. It serves as a foundational tool for future red team and penetration testing projects and provides practical insight into how service discovery works at the TCP layer.

---

**Repository:** Add your GitHub repository URL here.
