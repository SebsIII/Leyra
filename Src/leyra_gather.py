#This script gathers data from the weather system 

import requests
import datetime
import json

IPA = "192.168.1.200"

def formatRawData(data):
    data = [data["Data"]["Temperature"], data["Data"]["Pressure"], data["Data"]["RainLevel"], data["Data"]["ApproxAltitude"], data["Millis"]]
    return data

response = requests.get("http://" + IPA)
dataArray = formatRawData(response.json())

time = datetime.datetime.now()
with open("../Playground/DataPack1.json", "r+") as f:
    file_data = json.load(f)
    file_data["Data"].update(dataArray)
    f.seek(0)
    json.dump(file_data, f, indent=4)

#{
#"Data": {
#  "Temperature":28.09,
#  "Pressure":101234.47,
#  "ApproxAltitude":7.54,
#  "RainLevel":0.00
#},
#"Millis":277042,
#"DaysPassed":0,
#"IWSmessage":"All clear."
#}


