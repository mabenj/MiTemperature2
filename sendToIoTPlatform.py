#! /usr/bin/python3
 
import sys, requests, os
 
url = os.environ.get("IOT_URL")
headers = {"Content-Type": "application/json; charset=utf-8"}
 
data = sys.argv[1].split(" ", 1)
 
keys = sys.argv[1].split(",")
values = sys.argv[2:]
 
json = {}
for i in range(len(keys)):
    json[keys[i]] = values[i]
 
r = requests.post(url=url, json=json, headers=headers)
 
# cron
# */30 * * * * /usr/bin/python3 /home/marko/MiTemperature2/LYWSD03MMC.py --device A4:C1:38:09:3F:73 --count 1 --unreachable-count 50 --callback sendToIoTPlatform.py >> /home/marko/MiTemperature2/cron.log 2>&1