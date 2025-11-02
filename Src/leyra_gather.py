#This script gathers data from the weather system 

import requests
import datetime
import json
import time

IPA = "192.168.1.200"

def formatRawData(data):
    data = [data["Data"]["Temperature"], data["Data"]["Pressure"], data["Data"]["RainLevel"], data["Data"]["ApproxAltitude"], data["Millis"]]
    return data

def getAndSave():
    response = requests.get("http://" + IPA)
    dataArray = formatRawData(response.json())

    day = datetime.datetime.now().strftime("%d-%m-%y")
    try: 
        time = datetime.datetime.now().strftime("%H:%M ")
        with open(f"../Playground/{day}.json", "x+") as file:
            file.write("{\n}")
            file.seek(0)
            file_data = json.load(file)
            file_data["DaysPassed"] = response.json()["DaysPassed"]
            file_data[str(time)] = dataArray
            file.seek(0)
            json.dump(file_data, file, indent=4)

    except FileExistsError:
        with open(f"../Playground/{day}.json", "r+") as file:
            file_data = json.load(file)
            file_data[str(time)] = dataArray
            file.seek(0)
            json.dump(file_data, file, indent=4)

print("Starting Polling...")
while True:
    getAndSave()
    time.sleep(180)

