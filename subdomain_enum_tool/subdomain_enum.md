# Subdomain Enumeration Tool
**Date:** 2026-06-19

## Overview

I created a Python-based Subdomain Enumeration Tool to automate the discovery of valid subdomains for a target domain. The tool reads entries from a wordlist, appends them to the target domain, and checks whether the generated hostname responds to HTTP requests.

---

## Features

- Reads subdomain names from a custom wordlist
- Generates potential subdomains automatically
- Sends HTTP requests to test reachability
- Handles connection errors and timeouts gracefully
- Displays discovered subdomains in real-time
- Lightweight and easy to use

---

## Technologies Used

- Python 3
- requests
- sys

---

## How It Works

1. Load a wordlist containing possible subdomain names.
2. Append each entry to the target domain.
3. Send an HTTP request to the generated URL.
4. Record and display successful responses.

Example:

Target Domain:

example.com

Wordlist:

admin
mail
dev

Generated URLs:

http://admin.example.com
http://mail.example.com
http://dev.example.com

---

## Usage

```bash
python3 subdomain_enum.py <domain> <wordlist>
```

Example:

```bash
python3 subdomain_enum.py example.com subdomains.txt
```

---

## Sample Output

```text
[*] Starting subdomain enumeration for example.com
[*] Loaded 50 entries from subdomains.txt

[+] Found: http://admin.example.com
[+] Found: http://mail.example.com

[*] Enumeration complete. Found 2 subdomain(s).
```

---

## Skills Practiced

- Python Functions
- File Handling
- HTTP Requests
- Exception Handling
- Command-Line Arguments
- Cybersecurity Automation

---

## Future Improvements

- HTTPS support
- DNS validation
- Multithreading
- User-Agent customization
- Export results to files
- Status code filtering

---

## Conclusion

This project helped me gain hands-on experience with Python scripting and web reconnaissance by automating the process of subdomain discovery.
