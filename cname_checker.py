import socket
import os
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows compatibility
init(autoreset=True)

def print_banner():
    """Display program banner"""
    banner = f"""
{Fore.GREEN}╔══════════════════════════════════════════════════╗
{Fore.GREEN}║{Fore.YELLOW}         Subdomain CNAME Checker Tool            {Fore.GREEN}║
{Fore.GREEN}║{Fore.CYAN}       Check CNAME records for subdomains         {Fore.GREEN}║
{Fore.GREEN}╚══════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""
    print(banner)

def get_cname(subdomain):
    """Get CNAME record for a subdomain"""
    try:
        cname = socket.gethostbyname_ex(subdomain)
        return cname[0] if cname else None
    except socket.gaierror:
        return None
    except Exception as e:
        print(f"{Fore.RED}Error checking {subdomain}: {e}")
        return None

def process_subdomains(file_path):
    """Process subdomains from file"""
    if not os.path.exists(file_path):
        print(f"{Fore.RED}Error: File not found at {file_path}")
        return

    try:
        with open(file_path, 'r') as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"{Fore.RED}Error reading file: {e}")
        return

    if not subdomains:
        print(f"{Fore.YELLOW}No subdomains found in the file.")
        return

    print(f"\n{Fore.CYAN}Checking {len(subdomains)} subdomains...\n")

    for subdomain in subdomains:
        print(f"{Fore.WHITE}Subdomain: {Fore.YELLOW}{subdomain}")
        cname = get_cname(subdomain)
        
        if cname:
            print(f"{Fore.GREEN}CNAME points to: {Fore.WHITE}{cname}")
        else:
            print(f"{Fore.RED}No CNAME record found")
        print("-" * 50)

def main():
    print_banner()
    
    while True:
        file_path = input(f"{Fore.CYAN}Enter path to subdomains file (or 'exit' to quit): {Style.RESET_ALL}").strip()
        
        if file_path.lower() == 'exit':
            print(f"{Fore.YELLOW}Exiting program...")
            break
            
        process_subdomains(file_path)
        print(f"\n{Fore.GREEN}Check completed. You can enter another file or type 'exit' to quit.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program interrupted by user. Exiting...")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")