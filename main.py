from utils import print_banner
from unfollow import unfollow_nonfollowers

def main():
    print_banner()
    print("\n[1] Unfollow users who don’t follow you back")
    print("[2] Exit")

    choice = input("Select an option: ")
    if choice == "1":
        try:
            limit = int(input("How many to unfollow (max 50 recommended): "))
            if limit > 50:
                print("[!] Too many. Capping to 50 for safety.")
                limit = 50
        except:
            print("[×] Invalid number.")
            return

        unfollow_nonfollowers(limit)

    elif choice == "2":
        print("[*] Exiting...")
    else:
        print("[×] Invalid option.")

if __name__ == "__main__":
    main()
