#!/usr/bin/env python3
# ─────────────────────────────────────────────
#  WiFi Security Tool & Guide — by Sojib
# ─────────────────────────────────────────────

import sys
import os
import time

# ── Colors ──────────────────────────────────
R  = '\033[1;31m'   # red
G  = '\033[1;32m'   # green
Y  = '\033[1;33m'   # yellow
B  = '\033[1;34m'   # blue
M  = '\033[1;35m'   # magenta
C  = '\033[1;36m'   # cyan
W  = '\033[1;37m'   # white
RS = '\033[0m'       # reset

# ── Symbols ─────────────────────────────────
OK   = f'{G}[{W}+{G}]{RS}'
INFO = f'{B}[{W}i{B}]{RS}'
WARN = f'{Y}[{W}!{Y}]{RS}'
TIP  = f'{M}[{W}★{M}]{RS}'
CMD  = f'{C}[{W}>{C}]{RS}'

LINE  = f'{C}{"━"*52}{RS}'
LINE2 = f'{B}{"─"*52}{RS}'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def pause():
    input(f'\n{INFO} {W}Press Enter to go back to menu...{RS}')

# ── Your Custom Banner ──────────────────────
def banner():
    print(f'''{B}==========================================================
[!] INITIALIZING SECURE HACKING ENVIRONMENT...
[!] TARGET: WIRELESS VULNERABILITY ASSESSMENT
==========================================================

       (\\__/)
       (=\\'.\\'=)
       (\")_(\")

  ██╗  ██╗ █████╗ ███╗   ███╗███████╗████████╗███████╗██████╗ 
  ██║  ██║██╔══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
  ███████║███████║██╔████╔██║███████╗   ██║   █████╗  ██████╔╝
  ██╔══██║██╔══██║██║╚██╔╝██║╚════██║   ██║   ██╔══╝  ██╔══██╗
  ██║  ██║██║  ██║██║ ╚═╝ ██║███████║   ██║   ███████║██║  ██║
  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

[!] WARNING: FOR AUTHORIZED TESTING ONLY [!]

==========================================================
                    OWNER : SOJIB 😈
                    TG    : @NOCKS69
                    WP    : 01330132636

              Premium WiFi Tools 🥰
                 Contact To Buy
=========================================================={RS}''')

# ────────────────────────────────────────────
def show_menu():
    clear()
    banner()
    print(f'''{LINE}
{Y}  What do you want to do? Pick a number:{RS}
{LINE}

  {G}1{RS}  →  {W}What is WiFuX? Introduction{RS}
  {G}2{RS}  →  {W}How to Install / Setup{RS}
  {G}3{RS}  →  {W}What is an Interface & how to find it{RS}
  {G}4{RS}  →  {W}All Attack Modes explained{RS}
  {G}5{RS}  →  {W}Full Command List (A-Z){RS}
  {G}6{RS}  →  {W}Usage Examples (Copy-Paste ready){RS}
  {G}7{RS}  →  {W}Troubleshooting common errors{RS}
  {G}8{RS}  →  {W}Important warnings & rules{RS}
  
  {C}9  →  🚀 Start WiFi Scan / Attack (WiFuX){RS}

  {R}0{RS}  →  {W}Exit{RS}

{LINE}''')
    return input(f'  {C}Your choice: {RS}').strip()

def section_intro():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  1. What is WiFuX — Introduction{RS}
{LINE}
{INFO} {W}WiFuX{RS} is a WPS security testing tool that runs in Termux.
''')
    pause()

def start_wifi_tool():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  🚀 Starting WiFi Scanning & Attack Mode...{RS}
{LINE}
''')
    print(f"{INFO} Initializing wireless interface...\n")
    # এখানে আপনার মূল ওয়াইফাই স্ক্যানিং বা টুল রান করার কমান্ড দিন
    os.system('python main.py -i wlan0 -K')
    pause()

def main():
    handlers = {
        '1': section_intro,
        '9': start_wifi_tool,
    }

    while True:
        choice = show_menu()
        if choice == '0':
            clear()
            print(f'\n{M}  ★ Stay With Sojib — Thanks for using WiFi Tool!{RS}\n')
            sys.exit(0)
        elif choice in handlers:
            handlers[choice]()
        else:
            print(f'{WARN} {Y}Invalid choice! Please try again.{RS}')
            time.sleep(1)

if __name__ == '__main__':
    main()
	
