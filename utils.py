import time
from network_checker import check_internet
from recharge import auto_recharge

def auto_network_watchdog(interval=10):
    print("🔍 Auto network monitor started...")

    while True:
        if check_internet():
            print("✅ Internet active")
        else:
            print("❌ No Internet — Triggering auto recharge...")
            print(auto_recharge())
        time.sleep(interval)
