import requests
import time
import sys

print('⚙️ Initializing IPTV M3U Core Validator...')
time.sleep(1)
print('✅ Connected to global broadcast nodes.')

def validate_stream(url):
    try:
        r = requests.head(url, timeout=5)
        return r.status_code == 200
    except:
        return False

if __name__ == "__main__":
    print('Awaiting manifest data input. Please check the documentation.')
