# ARP Network Scanner
**Date:** 2026-06-19

## Overview

I created a Python-based ARP Network Scanner to discover live hosts on a local network using the Address Resolution Protocol (ARP). The tool broadcasts ARP requests across a specified IP range and collects responses from active devices.

This project provided hands-on experience with packet crafting, network discovery, and using the Scapy library for offensive security scripting.

---

## Features

- Discovers live hosts on a local network
- Displays IP and MAC addresses of active devices
- Uses ARP broadcast requests for fast host discovery
- Supports custom network ranges
- Allows selection of a network interface
- Lightweight and effective for internal reconnaissance

---

## Technologies Used

- Python 3
- Scapy
- sys

---

## How It Works

### Step 1: Create a Broadcast Packet

The tool builds an Ethernet frame targeting the broadcast MAC address:

```text
ff:ff:ff:ff:ff:ff
```

This ensures all devices on the local network receive the ARP request.

### Step 2: Generate an ARP Request

The ARP layer targets a specified IP range:

```python
ARP(pdst="10.10.10.0/24")
```

### Step 3: Send and Receive Packets

Using Scapy's `srp()` function, the scanner:

- Sends ARP requests
- Waits for responses
- Collects information from active hosts

### Step 4: Display Results

For every responding device, the scanner extracts:

- IP Address
- MAC Address

---

## Usage

```bash
sudo python3 arp_scanner.py <ip_range> [interface]
```

Example:

```bash
sudo python3 arp_scanner.py 10.10.10.0/24 eth0
```

---

## Sample Output

```text
[*] Scanning 10.10.10.0/24 on interface eth0...

[*] Found 3 live host(s):

IP Address          MAC Address
----------------------------------------
10.10.10.1          00:50:56:c0:00:08
10.10.10.5          00:50:56:c0:00:01
10.10.10.10         00:50:56:c0:00:02
```

---

## Skills Practiced

### Python Skills

- Function Creation
- Command-Line Arguments
- Data Structures
- Looping Through Responses
- Modular Script Development

### Networking Skills

- ARP Protocol Fundamentals
- Layer 2 Network Communication
- MAC Address Discovery
- Local Network Enumeration
- Host Discovery Techniques

### Cybersecurity Skills

- Internal Network Reconnaissance
- Asset Discovery
- Enumeration Automation
- Packet Crafting with Scapy
- Network Visibility and Mapping

---

## Key Concepts Learned

### ARP (Address Resolution Protocol)

ARP is used to map IP addresses to MAC addresses within a local network.

Example:

```text
Who has 10.10.10.5?
Tell 10.10.10.100
```

The target host responds with its MAC address, allowing communication to occur at Layer 2.

---

### Broadcast Traffic

The scanner uses Ethernet broadcast frames to reach every device on the subnet.

```text
ff:ff:ff:ff:ff:ff
```

All hosts receive the request, but only the target IP responds.

---

### Packet Crafting with Scapy

Scapy allows custom packet creation and network interaction directly from Python.

Example:

```python
packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
```

This combines Ethernet and ARP layers into a single packet.

---

## Challenges Encountered

- Understanding Ethernet and ARP packet structures
- Working with Scapy packet layers
- Handling network interface selection
- Parsing responses from active hosts
- Running scripts with elevated privileges

---

## Future Improvements

Planned enhancements include:

- Vendor lookup from MAC addresses
- Hostname resolution
- Export results to CSV/TXT
- Multi-threaded scanning
- OS fingerprinting integration
- Network inventory reporting
- Colored terminal output
- Live scan statistics

---

## Security Applications

This scanner can be useful for:

- Internal Network Discovery
- Asset Inventory
- Red Team Reconnaissance
- Blue Team Asset Verification
- Lab Environment Enumeration
- Network Troubleshooting

---

## Conclusion

Building this ARP Network Scanner strengthened my understanding of networking fundamentals, packet crafting, and host discovery techniques. It also provided practical experience using Scapy to automate reconnaissance tasks commonly performed during penetration testing and internal network assessments.

This project serves as a foundation for more advanced network scanning and enumeration tools in future cybersecurity projects.
