import time
import random

def delay(min_sec=8, max_sec=15):
    wait = random.randint(min_sec, max_sec)
    print(f"[⏳] Waiting {wait}s before next action...")
    time.sleep(wait)

def print_banner():
    print(r"""
██████╗  ██████╗     ██╗   ██╗███╗   ██╗███████╗ █████╗ ██╗     ██╗
██╔══██╗██╔═══██╗    ██║   ██║████╗  ██║██╔════╝██╔══██╗██║     ██║
██████╔╝██║   ██║    ██║   ██║██╔██╗ ██║█████╗  ███████║██║     ██║
██╔═══╝ ██║   ██║    ██║   ██║██║╚██╗██║██╔══╝  ██╔══██║██║     ██║
██║     ╚██████╔╝    ╚██████╔╝██║ ╚████║███████╗██║  ██║███████╗███████╗
╚═╝      ╚═════╝      ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
        Safe IG Unfollower - Termux Edition
""")
