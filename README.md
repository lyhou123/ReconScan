# ReconScan: Advanced Port Scanner Tool

**ReconScan** is a powerful, multi-threaded port scanner built in Python for network reconnaissance and security research. It scans a range of ports on a target system, grabs banners from open ports to identify services, and logs the results for further analysis.

This tool is intended for **ethical hacking** and **security testing** only. Please ensure you have explicit permission to scan the target system.

## Features

- **Multi-threaded**: Speeds up the scanning process by scanning multiple ports simultaneously.
- **Banner Grabbing**: Retrieves service banners from open ports for service identification.
- **Custom Port Range**: Scan a user-defined range of ports.
- **Verbose Output**: Show closed ports and errors (optional).
- **Logging**: Save results to a file (`scan_results.txt`).
- **Cross-platform**: Works with Git Bash, PowerShell, and WSL on Windows.

## Requirements

- Python 3.x
- Git Bash (if using Windows)
- (Optional) WSL for a more native Linux environment

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lyhou123/ReconScan.git
   cd ReconScan
   python reconsan.py <target_ip> -s <start_port> -e <end_port> -t <threads> [-v]
