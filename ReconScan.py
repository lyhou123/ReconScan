import socket
import argparse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

#banner grabbing function
def grab_banner(ip, port):
    try:
        with socket.socket() as s:
            s.settimeout(2)
            s.connect((ip, port))
            banner = s.recv(1024).decode().strip()
            if banner:
                print(f"[+] {ip}:{port} - {banner}")
            return banner       
    except (socket.timeout, ConnectionRefusedError):
        pass
    except Exception as e:
        print(f"[-] Error: {e}")
        return None


# Port scanning function
def scan_port(ip, port, verbose=False):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                banner = grab_banner(ip, port)
                service = f"banner: {banner}" if banner else "No banner"
                output = f"[+] Port {port} is open - {service}"
                print(output)
                with open("scan_result.txt", "a") as f:
                    f.write(f"{ip}:{port} - OPEN - {service}\n")                    
            elif verbose:
                print(f"[-] Port {port} is closed")
                return None
    except socket.timeout:
        print(f"[-] Port {port} timed out")
        return None
    except Exception as e:
        if verbose:
            print(f"[-] Error: {e} - Port {port}")
            return None            
        
#main scan running routine 
def run_scan(target_ip, start_port, end_port, max_threads, verbose):
    try:
        hostname = socket.gethostbyaddr(target_ip)[0]
    except:
        hostname = "Unknown"
    
    print(f"\n[***] Scanning target: {target_ip} ({hostname})")
    print(f"[***] Port range: {start_port}-{end_port}")
    print(f"[***] Starting scan at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    
    with ThreadPoolExecutor(max_workers=max_threads) as executer:
        for port in range (start_port, end_port + 1):
            executer.submit(scan_port, target_ip, port, verbose)
                    

#Argument parsing
def main():
    
    parser = argparse.ArgumentParser(description="Advanced Port Scanner (ReconScan)")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads (default: 100)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output (show closed ports)")

    args = parser.parse_args()
    
    try:
        ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print("Invalide host Name !!") 
        return None

if __name__=="__Main__":
    main();
    
           