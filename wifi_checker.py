import random

# Temporarily simulating WiFi network loss
def check_wifi_status():
    status = random.choice(["wifi_ok", "wifi_off"])
    return status
#Later this will connect with system Wifi API/Socket listner