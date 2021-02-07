import os
os.sys.path.append("c:\python38\lib\site-packages")
os.sys.path.append("c:\\users\\hbeny\\appdata\\roaming\\python\\python38\\site-packages")
import subprocess
import requests
import json
import colorama

print("""
 | \ | |    | |                    | |    |__   __|                               | |      
 |  \| | ___| |___      _____  _ __| | __    | |_ __ __ _  ___ ___ _ __ ___  _   _| |_ ___ 
 | . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /    | | '__/ _` |/ __/ _ \ '__/ _ \| | | | __/ _ \\
 | |\  |  __/ |_ \ V  V / (_) | |  |   <     | | | | (_| | (_|  __/ | | (_) | |_| | ||  __/
 |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\    |_|_|  \__,_|\___\___|_|  \___/ \__,_|\__\___|
""")
target = input("Enter a link or IP: ")
print("If it takes a while, don't panic! Doing a network traceroute usually takes a while. Make sure you are connected to the internet!\n\n")
tracer = subprocess.check_output(['tracert', target]).decode().splitlines()
for x in range(2):
    tracer.pop(1)
for x in range(len(tracer) - 1):
    if (len(tracer[x].split(" ")) - 1) > 0:
        try:
            ip = tracer[x].split("  ")[8].split(" ")[0]
        except:
            ip = tracer[x].split("  ")[7].split(" ")[0]
        infoapireq = requests.get("http://ip-api.com/json/" + ip)
        res = json.loads(infoapireq.text)
        a = res.get("as")
        country = res.get("country")
        city = res.get("city")
        org = res.get("org")
        print(f"IP: {ip}, Country: {country}, City: {city}, Company: {a}, {org}")
