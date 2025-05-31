from instagrapi import Client
import config
from datetime import datetime
from utils import delay

def unfollow_nonfollowers(limit=50):
    cl = Client()
    try:
        cl.login(config.USERNAME, config.PASSWORD)
    except Exception as e:
        print(f"[!] Login failed: {e}")
        return

    user_id = cl.user_id
    print(f"[*] Logged in as @{config.USERNAME}")

    print("[*] Fetching following...")
    following = cl.user_following(user_id)

    print("[*] Fetching followers...")
    followers = cl.user_followers(user_id)

    non_followers = [user for user in following.values() if user.pk not in followers]
    print(f"[!] Found {len(non_followers)} users not following back.")

    limit = min(limit, len(non_followers))
    confirm = input(f"Proceed to unfollow {limit} users? (y/n): ").lower()
    if confirm != "y":
        print("[×] Cancelled.")
        return
