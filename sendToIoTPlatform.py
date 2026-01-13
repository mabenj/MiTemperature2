#! /usr/bin/python3

import sys, requests, psutil, time

url = "<URL>"
device = "<DEVICE>"
headers = {"Content-Type": "application/json; charset=utf-8"}

data = sys.argv[1].split(" ", 1)

keys = sys.argv[1].split(",")
values = sys.argv[2:]

sensor_name_index = keys.index("sensorname")
if(values[sensor_name_index] != device):
    print("Device does not match")
    exit(1)

json = {}
for i in range(len(keys)):
    json[keys[i]] = values[i]

r = requests.post(url=url, json=json, headers=headers)

time.sleep(10)

for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] == 'bluepy-helper':
        pid = proc.info['pid']
        print(f"Killing bluepy-helper (pid:{pid})")
        process = psutil.Process(pid)
        process.terminate()