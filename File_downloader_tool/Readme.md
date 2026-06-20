# Downloader Tool Documentation

**Date:** 20 June 2026

## Overview

The Downloader Tool is a Python utility that downloads files from either a single URL or a text file containing multiple URLs. It uses the Requests library for handling HTTP requests and automatically saves downloaded files locally.

## Features

* Download files from a single URL
* Download multiple files from a URL list
* Automatic filename detection
* Creates download directory automatically
* Handles redirects
* Timeout protection
* HTTP error handling
* Download summary statistics

## Requirements

### Python Version

* Python 3.x

### Dependencies

Install the required dependency:

```bash
pip install requests
```

---

## Usage

### Download a Single File

```bash
python3 downloader.py https://example.com/file.zip
```

Example:

```bash
python3 downloader.py https://downloads.example.com/tool.zip
```

Output:

```text
[+] Downloaded: tool.zip (125478 bytes)
```

---

### Download Multiple Files Using a URL List

Create a text file containing one URL per line.

Example file:

**urls.txt**

```text
https://example.com/file1.zip
https://example.com/file2.pdf
https://example.com/file3.txt
```

Save the file anywhere on your system.

Examples:

```text
/home/user/urls.txt
```

```text
/opt/lists/download_targets.txt
```

```text
/root/wordlists/urls.txt
```

Run the tool by providing the path to the URL file:

```bash
python3 downloader.py /home/user/urls.txt
```

Example output:

```text
[*] Loaded 3 URL(s) from /home/user/urls.txt

[+] Downloaded: file1.zip
[+] Downloaded: file2.pdf
[+] Downloaded: file3.txt

[*] Complete: 3 downloaded, 0 failed
```

---

## URL File Format

The URL file must contain one URL per line:

```text
https://example.com/report.pdf
https://example.com/image.png
https://example.com/archive.zip
```

Blank lines are ignored automatically.

---

## Download Directory Structure

When using a URL list, downloaded files are stored inside:

```text
downloads/
├── report.pdf
├── image.png
├── archive.zip
```

The directory is created automatically if it does not already exist.

---

## Error Handling

### Connection Error

```text
[!] Connection failed: https://example.com/file.zip
```

### Timeout Error

```text
[!] Request timed out: https://example.com/file.zip
```

### HTTP Error

```text
[!] HTTP error: 404 Client Error
```

---

## Functions

### download_file(url, output_path)

Downloads a file from a URL and saves it locally.

#### Parameters

| Parameter   | Description     |
| ----------- | --------------- |
| url         | Target file URL |
| output_path | Local save path |

#### Returns

```python
True
```

if successful, otherwise:

```python
False
```

---

### download_from_list(url_list, output_dir="downloads")

Downloads files from multiple URLs.

#### Parameters

| Parameter  | Description                     |
| ---------- | ------------------------------- |
| url_list   | List of URLs                    |
| output_dir | Directory where files are saved |

#### Returns

```python
{
    "success": 5,
    "failed": 1
}
```

---

## Example Workflow

### Step 1

Create a URL list file:

```text
https://example.com/file1.zip
https://example.com/file2.pdf
https://example.com/file3.txt
```

### Step 2

Save it as:

```text
/home/user/urls.txt
```

### Step 3

Run:

```bash
python3 downloader.py /home/user/urls.txt
```

### Step 4

Files will be downloaded to:

```text
downloads/
```

---

## Security Considerations

* Download files only from trusted sources.
* Verify downloaded files using hashes when available.
* Be cautious with executable files.
* Ensure adequate disk space before large downloads.
* Avoid downloading sensitive data from unknown sources.

---

## Sample Output

```text
[*] Loaded 4 URL(s) from /home/user/urls.txt

[+] Downloaded: report.pdf (52134 bytes)
[+] Downloaded: image.png (18344 bytes)
[+] Downloaded: archive.zip (992145 bytes)

[!] HTTP error: 404 Client Error

[*] Complete: 3 downloaded, 1 failed
```

---

## Author

Created as part of Python for Pentesters practice and automation toolkit development.

**Tool Name:** Downloader Tool
**Language:** Python 3
**Library Used:** Requests
