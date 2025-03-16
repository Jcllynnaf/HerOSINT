import argparse
import requests
import socket
import dns.resolver
import whois
import time
import nmap
import shutil
import sys
import threading
import os
from termcolor import colored

def print_banner():
    """Print a tool banner."""
    banner = """
\033[31m
 ██░ ██ ▓█████  ██▀███   ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▒██▀▀██░▒███   ▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░▓█▒░██▓░▒████▒░██▓ ▒██▒░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
 ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
 ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
 ░  ░░ ░   ░     ░░   ░ ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
 ░  ░  ░   ░  ░   ░         ░ ░        ░   ░           ░          
                                                                  
\033[31m
╭────────────────────────────────────────────────────╮
│                  OSINT IP Scanner                  │
│                                                    │
│     Status    : v 1.1 Free Tool                    │
│     GitHub    : https://github.com/jcllynnaf       │
│     Support   : https://linktr.ee/jcllynnaf        │
│     instagram : https://instagram.com/jcllynnaf    │
╰────────────────────────────────────────────────────╯
\033[0m
    """
    print(colored(banner, "red"))

def print_intro():
   
    intro_text = """
\033[31m
╔═══════════════════════════════════════════════════╗
║             WELCOME TO HerOSINT TOOL              ║
║  This tool is designed for OSINT investigations,  ║
║  providing various techniques for IP analysis,    ║
║  reconnaissance, and target information gathering ║
║                                                   ║
║           Press Enter to continue...              ║
╚═══════════════════════════════════════════════════╝
\033[0m
"""
    print(colored(intro_text, "red"))
    input()

def clear_screen():
    """Clean the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_loading(message, stop_event, delay=0.1):
    
    animation = "|/-\\"
    idx = 0
    while not stop_event.is_set():  # Check the event to stop
        print(colored(f"\r{message} {animation[idx % len(animation)]}", "red"), end="", flush=True)
        idx += 1
        time.sleep(delay)
    print(colored("\r", "red"), end="", flush=True)  # Delete animation after stopping

def loading_message():
   
    loading_text = "[+] Check dependencies and connections..."
    stop_event = threading.Event()  # Create an event
    loading_thread = threading.Thread(target=animated_loading, args=(loading_text, stop_event))
    loading_thread.start()
    time.sleep(3)  # Simulation of dependence checking
    stop_event.set()  # Event set to stop animation
    loading_thread.join()  # Wait for the thread to finish
    print(colored("\r[OK] All dependencies are available!                                     \n", "red"), end="", flush=True)
    time.sleep(1)

def dns_enumeration(domain):
    
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Performing DNS Enumeration...", stop_event))
    loading_thread.start()
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
        answers = resolver.resolve(domain, 'A')
        stop_event.set()  # Set event to stop animation
        loading_thread.join()
        print(colored("\r[OK] DNS Enumeration is complete!                                      \n", "red"), end="", flush=True)
        print(colored("[+] Looking for IP leaks from DNS...", "red"))
        for rdata in answers:
            print(colored(f"[FOUND] DNS Enumeration: {rdata}", "red"))
    except Exception as e:
        stop_event = threading.Event()
        loading_thread = threading.Thread(target=animated_loading, args=("[+] Performing DNS Enumeration...", stop_event))
        loading_thread.start()
        print(colored("\r[!] DNS Enumeration failed!                                        \n", "red"), end="", flush=True)
        print(colored(f"[!] DNS Enumeration failed: {e}", "red"))

def historical_ip_lookup(domain):
    
    print(colored("[+] Search for IP history...", "red"))
    try:
        # **IMPORTANT:** Replace YOUR_API_KEY with your SecurityTrails API key.!
        api_key = "F6Xpv0hYeBE0tMqylzkjq79vbuGJh55J"  
        url = f"https://api.securitytrails.com/v1/domain/{domain}/history?apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "records" in data:
                for record in data["records"]:
                    print(colored(f"[FOUND] Historical IP: {record['ip']}", "red"))
            else:
                print(colored("[!] No IP history data found", "red"))
        else:
            print(colored(f"[!] Error: {response.text}", "red"))
    except Exception as e:
        print(colored(f"[!] Historical IP Lookup failed: {e}", "red"))

def direct_ip_leak(domain):
  
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Trying Direct IP Leak...", stop_event))
    loading_thread.start()
    try:
        ip = socket.gethostbyname(domain)
        stop_event.set()
        loading_thread.join()
        print(colored("\r[OK] Direct IP Leak completed!                                      \n", "red"), end="", flush=True)
        print(colored("[+] Trying to find the original IP...", "yellow"))
        print(colored(f"[FOUND] Direct IP: {ip}", "red"))
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(colored("\r[!] Direct IP Leak failed!                                        \n", "red"), end="", flush=True)
        print(colored(f"[!] failed to find the original IP: {e}", "red"))

def whois_lookup(domain):
  
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Performing a WHOIS Lookup...", stop_event))
    loading_thread.start()
    try:
        info = whois.whois(domain)
        stop_event.set()
        loading_thread.join()
        print(colored("\r[OK] WHOIS Lookup completed!                                        \n", "red"), end="", flush=True)
        print(colored("[+] Performing a WHOIS Lookup...", "yellow"))
        print(colored(f"WHOIS Data:\n{info}", "red"))
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(colored("\r[!] WHOIS Lookup failed!                                          \n", "red"), end="", flush=True)
        print(colored(f"[!] WHOIS Lookup failed: {e}", "red"))

def port_scanning(domain):
 
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Scanning for open ports...", stop_event))
    loading_thread.start()
    try:
        scanner = nmap.PortScanner()
        # Hanya pindai port yang umum dan gunakan argumen yang lebih agresif
        scanner.scan(domain, '21,22,80,443,3389', arguments='-T4')
        stop_event.set()
        loading_thread.join()
        print(colored("\r[OK] Port Scanning completed!                                       \n", "green"), end="", flush=True)
        print(colored("[+] Scanning for open ports...", "yellow"))
        for host in scanner.all_hosts():
            print(colored(f"[FOUND] Host: {host}", "red"))
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    print(colored(f" - Port {port}: {scanner[host][proto][port]['state']}", "red"))
            break  # Hanya tampilkan informasi untuk host pertama
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(colored("\r[!] Port Scanning failed!                                         \n", "red"), end="", flush=True)
        print(colored(f"[!] Port Scanning failed: {e}", "red"))

def menu():
   
    global domain

    # Set the color for the menu text
    menu_color = "\033[31m"  #red
    reset_color = "\033[0m"   # Reset to the default color

    while True:
        print_banner()

        # Create a menu with the desired line characters
        print(colored(menu_color + "╔════════════════════════════════════╗", "red"))
        print(colored(menu_color + "║ [1] Enter Target Domain            ║", "red"))
        print(colored(menu_color + "║ [2] DNS Enumeration                ║", "red"))
        print(colored(menu_color + "║ [3] Historical IP Lookup           ║", "red"))
        print(colored(menu_color + "║ [4] Direct IP Leak                 ║", "red"))
        print(colored(menu_color + "║ [5] WHOIS Lookup                   ║", "red"))
        print(colored(menu_color + "║ [6] Port Scanning                  ║", "red"))
        print(colored(menu_color + "║ [7] Exit                           ║", "red"))
        print(colored(menu_color + "╚════════════════════════════════════╝" + reset_color, "red"))

        choice = input(colored("Enter options (1-7): ", "red"))
        if choice == "7":
            print(colored("GOOD BYE FRIEND ", "red"))
            break
        elif choice == "1":
            domain = input(colored("Enter Target Domain: ", "red"))
        elif choice in feature_mapping and domain:
            feature_mapping[choice](domain)
            input(colored("\nPress Enter to return to the main menu....", "red"))
        elif choice in feature_mapping and not domain:
            print(colored("[!] Please enter the domain first!", "red"))
        else:
            print(colored("[!] Invalid choice!", "red"))

def main():
  
    parser = argparse.ArgumentParser(description="Bypass Cloudflare & Find Real IP")
    parser.add_argument("-d", "--domain", help="Domain target")
    args = parser.parse_args()
    
    global domain
    domain = args.domain if args.domain else ""
    print_banner()  # Show banner
    print_intro()   # Show intro
    clear_screen()  # Clean the screen after the intro
    loading_message()  # Show loading messages
    menu()  # Show menus

# Mapping features to the function
feature_mapping = {
    "2": dns_enumeration,
    "3": historical_ip_lookup,
    "4": direct_ip_leak,
    "5": whois_lookup,
    "6": port_scanning
}

if __name__ == "__main__":
    import os
    main()
