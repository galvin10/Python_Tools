# Directory Enumeration Tool
**Date:** 2026-06-19

## Overview

I created a Python-based Directory Enumeration Tool to automate the discovery of hidden directories and files on web servers. The tool reads entries from a wordlist, appends them to a target URL, and identifies valid resources based on HTTP response codes.

---

## Features

- Custom wordlist support
- Optional file extension selection
- Detects valid directories and files
- Ignores 404 responses
- Displays HTTP status codes
- Handles connection failures and timeouts

---

## Technologies Used

- Python 3
- requests
- sys

---

## How It Works

1. Load directory/file names from a wordlist.
2. Append each entry to the target URL.
3. Add a file extension if specified.
4. Send HTTP requests.
5. Display valid responses.

Example:

Target:

http://target.com

Wordlist:

admin
login
backup

Extension:

.html

Generated Requests:

http://target.com/admin.html
http://target.com/login.html
http://target.com/backup.html

---

## Usage

```bash
python3 dir_enum.py <target_url> <wordlist> [extension]
```

Example:

```bash
python3 dir_enum.py http://10.10.10.5 wordlist.txt .html
```

---

## Sample Output

```text
[*] Starting directory enumeration for http://10.10.10.5
[*] Loaded 100 entries from wordlist.txt

[+] 200 - http://10.10.10.5/admin.html
[+] 403 - http://10.10.10.5/backup.html

[*] Enumeration complete. Found 2 valid path(s).
```

---

## Skills Practiced

- Python Scripting
- Web Enumeration
- HTTP Response Analysis
- File Handling
- Exception Handling
- Security Automation

---

## Future Improvements

- Recursive directory discovery
- Multithreading support
- HTTPS support
- Custom headers
- Output to CSV/TXT files
- Progress indicators
- Rate limiting controls

---

## Conclusion

This project provided practical experience in Python scripting and web application reconnaissance by automating directory and file discovery techniques commonly used during penetration testing.
