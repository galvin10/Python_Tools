# Hash Cracker Tool

**Date:** 20 June 2026

## Overview

Hash Cracker is a Python-based dictionary attack tool that attempts to recover plaintext values from cryptographic hashes using a supplied wordlist.

The tool reads candidate passwords from a wordlist, generates hashes using a selected algorithm, and compares them against a target hash until a match is found or the wordlist is exhausted.

This project was developed as part of Python for Pentesters practice and cybersecurity learning.

---

## Features

* Supports multiple hashing algorithms
* Dictionary-based password cracking
* Real-time hash generation output
* Displays number of attempts before success
* Simple command-line interface
* Error handling for invalid files
* Supports common hash formats

---

## Supported Algorithms

| Algorithm | Supported |
| --------- | --------- |
| MD5       | ✅         |
| SHA1      | ✅         |
| SHA256    | ✅         |
| SHA512    | ✅         |

---

## Requirements

### Python Version

* Python 3.x

### Libraries Used

The tool only uses Python standard libraries:

```python
hashlib
sys
```

No additional installation is required.

---

## Usage

### Syntax

```bash
python3 hash_cracker.py <hash> <wordlist> [algorithm]
```

### Parameters

| Parameter | Description                  |
| --------- | ---------------------------- |
| hash      | Target hash value            |
| wordlist  | Path to wordlist file        |
| algorithm | Hashing algorithm (optional) |

Default algorithm:

```text
md5
```

---

## Examples

### MD5

```bash
python3 hash_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 wordlist.txt md5
```

### SHA1

```bash
python3 hash_cracker.py 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd wordlist.txt sha1
```

### SHA256

```bash
python3 hash_cracker.py <sha256_hash> wordlist.txt sha256
```

### Default MD5

```bash
python3 hash_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 wordlist.txt
```

---

## Wordlist Location

The wordlist can be stored anywhere on the system.

Examples:

```bash
python3 hash_cracker.py HASH ./wordlist.txt md5
```

```bash
python3 hash_cracker.py HASH /home/user/wordlists/rockyou.txt sha1
```

```bash
python3 hash_cracker.py HASH /opt/wordlists/common.txt sha256
```

---

## Obtaining Wordlists

This tool requires a password wordlist for dictionary attacks.

Recommended open-source sources include:

### RockYou

RockYou is commonly included with Kali Linux.

Location:

```text
/usr/share/wordlists/rockyou.txt
```

If compressed:

```bash
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
```

---

### SecLists

SecLists is one of the most widely used open-source collections of security assessment wordlists.

Repository:

https://github.com/danielmiessler/SecLists

Useful locations:

```text
SecLists/Passwords/Common-Credentials/
SecLists/Passwords/Leaked-Databases/
SecLists/Usernames/
```

Clone SecLists:

```bash
git clone https://github.com/danielmiessler/SecLists.git
```

---

## Wordlist Format

The wordlist should contain one password candidate per line.

Example:

```text
password
admin
welcome
letmein
Password123
```

Blank lines are automatically ignored.

---

## Example Execution

Command:

```bash
python3 hash_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 wordlist.txt md5
```

Output:

```text
[*] Target hash: 5f4dcc3b5aa765d61d8327deb882cf99
[*] Algorithm: md5
[*] Wordlist: wordlist.txt
[*] Cracking...

[*] admin -> 21232f297a57a5a743894a0e4a801fc3
[*] letmein -> 0d107d09f5bbe40cade3de5c71e9e9b7
[*] password -> 5f4dcc3b5aa765d61d8327deb882cf99

[+] Match found after 3 attempts!
[+] Plaintext: password

[*] Hash cracked successfully.
```

---

## Functions

### compute_hash()

Generates a hash from a plaintext string.

```python
compute_hash(text, algorithm="md5")
```

Returns:

```python
hexdigest()
```

---

### crack_hash()

Attempts to recover plaintext from a target hash.

```python
crack_hash(target_hash, wordlist_path, algorithm="md5")
```

Returns:

```python
plaintext
```

or

```python
None
```

if no match is found.

---

## Limitations

* Dictionary attacks only
* Cannot crack hashes absent from the wordlist
* No brute-force mode
* No GPU acceleration
* Performance depends on wordlist size

---

## Security Considerations

* Use only in environments where you have explicit authorization.
* Intended for cybersecurity education, labs, CTFs, and authorized security assessments.
* Do not use against systems or accounts without permission.
* Large wordlists may require significant processing time.

---

## Future Improvements

* Multi-threaded cracking
* Progress indicators
* Automatic hash type detection
* Salt support
* Export results to file
* Support for bcrypt
* Support for Argon2
* Rule-based word mutations

---

## Sample Workflow

### Step 1

Identify the target hash.

```text
5f4dcc3b5aa765d61d8327deb882cf99
```

### Step 2

Obtain a wordlist from:

* RockYou
* SecLists
* Custom password lists

### Step 3

Run the tool.

```bash
python3 hash_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 rockyou.txt md5
```

### Step 4

Review the result.

```text
[+] Plaintext: password
```

---

## Author

Created as part of Python for Pentesters and offensive security learning.

**Tool Name:** Hash Cracker
**Language:** Python 3
**Libraries:** hashlib, sys
