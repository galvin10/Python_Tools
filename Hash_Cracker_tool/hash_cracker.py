import hashlib
import sys

def compute_hash(text, algorithm="md5"):
    """Compute the hash of a string using the specified algorithm."""
    h = hashlib.new(algorithm)
    h.update(text.encode())
    return h.hexdigest()

def crack_hash(target_hash, wordlist_path, algorithm="md5"):
    """Attempt to find the plaintext for a hash using a wordlist."""
    try:
        with open(wordlist_path, "r") as f:
            for line_number, line in enumerate(f, start=1):
                candidate = line.strip()
                if not candidate:
                    continue

                candidate_hash = compute_hash(candidate, algorithm)
                print(f"[*] {candidate} -> {candidate_hash}")  # show work

                if candidate_hash == target_hash.lower():
                    print(f"[+] Match found after {line_number} attempts!")
                    print(f"[+] Plaintext: {candidate}")
                    return candidate

        print(f"[-] Exhausted wordlist. No match found.")
        return None

    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
        return None

def main():
    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} <hash> <wordlist> [algorithm]")
        print(f"Example: python3 {sys.argv[0]} 5f4dcc3b5aa765d61d8327deb882cf99 wordlist.txt md5")
        print(f"Supported: md5, sha1, sha256, sha512")
        sys.exit(1)

    target_hash = sys.argv[1]
    wordlist_path = sys.argv[2]
    algorithm = sys.argv[3] if len(sys.argv) > 3 else "md5"

    print(f"[*] Target hash: {target_hash}")
    print(f"[*] Algorithm:   {algorithm}")
    print(f"[*] Wordlist:    {wordlist_path}")
    print(f"[*] Cracking...\n")

    result = crack_hash(target_hash, wordlist_path, algorithm)

    if result:
        print(f"\n[*] Hash cracked successfully.")
    else:
        print(f"\n[*] Try a larger wordlist or a different algorithm.")

main()
