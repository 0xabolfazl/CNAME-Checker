import socket
import os
from colorama import init, Fore, Style
from pyfiglet import figlet_format

# Initialize colorama for Windows compatibility
init(autoreset=True)

def print_banner():
    """Display large stylized banner"""
    banner = figlet_format("CNAME Checker", font="slant")
    print(f"{Fore.RED}{banner}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Subdomain CNAME Record Analyzer")
    print(f"{Fore.CYAN}{'-' * 40}{Style.RESET_ALL}\n")

def get_cname(subdomain):
    """Get CNAME record for a subdomain"""
    try:
        result = socket.gethostbyname_ex(subdomain)
        return result[0]  # Returns the canonical name
    except socket.gaierror:
        return None
    except Exception as e:
        print(f"{Fore.RED}Error checking {subdomain}: {e}")
        return None

def process_subdomains(file_path):
    """Process subdomains from file"""
    if not os.path.exists(file_path):
        print(f"{Fore.RED}Error: File not found at {file_path}")
        return False

    try:
        with open(file_path, 'r') as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{Fore.RED}Error reading file: {e}")
        return False

    if not subdomains:
        print(f"{Fore.YELLOW}No valid subdomains found in the file.")
        return False

    print(f"{Fore.CYAN}Checking {len(subdomains)} subdomains...\n")

    for subdomain in subdomains:
        print(f"{Fore.WHITE}[+] Subdomain: {Fore.YELLOW}{subdomain}")
        cname = get_cname(subdomain)
        
        if cname and cname != subdomain:
            print(f"{Fore.GREEN}  ↳ CNAME: {Fore.WHITE}{cname}")
        else:
            print(f"{Fore.RED}  ↳ No CNAME record found")
        print(f"{Fore.BLUE}{'-' * 50}{Style.RESET_ALL}")

    return True

def main():
    print_banner()
    
    while True:
        file_path = input(f"{Fore.CYAN}Enter subdomains file path (or 'exit' to quit): {Style.RESET_ALL}").strip()
        
        if file_path.lower() == 'exit':
            print(f"{Fore.YELLOW}\nExiting program...")
            break
            
        success = process_subdomains(file_path)
        
        if success:
            print(f"{Fore.GREEN}\nScan completed. You can check another file or type 'exit' to quit.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program interrupted by user. Exiting...")
        exit()
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")
        exit(1)