#Check If Installed
import os
try: 
    import requests  
except ImportError: 
    print("Requests Not Found...\nInstalling...")
    os.system("pip install requests")
    print("Requests Installed")
#import
import random
from keepalive import keep_alive
import string
import time
import requests
#start the gen
print("Gamer's Nitro Generator\nDiscord: Gamer3514#7679\nIf you like this tool give it a star on github!")
time.sleep(0.75)
print("Starting The Gen...")
time.sleep(2.5)
print("Gen Started. Enjoy!")
#gen codes
def gencode():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(19))

class Generator:
    def __init__(self):
        self.codes = []
        self.check()

    def check(self):
        while True:
            code = gencode()
            self.codes.append(code)
            response = requests.get(
                f"https://discord.com/api/v7/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
            )
            data = response.json()
            if data["message"] == 'Unknown Gift Code':
                print(f"Invalid: {code}")
            else:
                print(f'Rate Limited: {code}')
                print('Waiting For Rate Limit To Go Away...')
                print(data)
                time.sleep(int(data['retry_after'])/1000)

keep_alive()
Generator()
