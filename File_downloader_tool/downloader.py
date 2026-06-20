import requests
import sys
import os

def download_file(url, output_path):
    """Download a file from a URL and save it locally."""
    try:
        r = requests.get(url, allow_redirects=True, timeout=10)
        r.raise_for_status()

        with open(output_path, "wb") as f:
            f.write(r.content)

        print(f"[+] Downloaded: {output_path} ({len(r.content)} bytes)")
        return True

    except requests.ConnectionError:
        print(f"[!] Connection failed: {url}")
        return False
    except requests.Timeout:
        print(f"[!] Request timed out: {url}")
        return False
    except requests.HTTPError as e:
        print(f"[!] HTTP error: {e}")
        return False

def download_from_list(url_list, output_dir="downloads"):
    """Download files from a list of URLs into the specified directory."""
    os.makedirs(output_dir, exist_ok=True)
    results = {"success": 0, "failed": 0}

    for url in url_list:
        filename = url.split("/")[-1]
        if not filename:
            filename = "index.html"
        output_path = os.path.join(output_dir, filename)

        if download_file(url, output_path):
            results["success"] += 1
        else:
            results["failed"] += 1

    print(f"\n[*] Complete: {results['success']} downloaded, {results['failed']} failed")
    return results

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <url_or_file>")
        print(f"  Single file:  python3 {sys.argv[0]} http://example.com/file.zip")
        print(f"  From list:    python3 {sys.argv[0]} urls.txt")
        sys.exit(1)

    target = sys.argv[1]

    if os.path.isfile(target):
        with open(target, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
        print(f"[*] Loaded {len(urls)} URL(s) from {target}")
        download_from_list(urls)
    else:
        filename = target.split("/")[-1] or "downloaded_file"
        download_file(target, filename)

main()
