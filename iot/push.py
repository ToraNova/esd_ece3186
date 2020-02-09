#!/usr/bin/python3
import requests
from time import sleep

wstr = None
mbool = None
mraw = None
lbool = None

with open("/home/pi/esd_ece3186/logs/water_percent.out","r") as f: 
    wstr = f.read()[:-1]
with open("/home/pi/esd_ece3186/logs/moist_bool.out","r") as f: 
    mbool = f.read()[:-1]
with open("/home/pi/esd_ece3186/logs/moist_raw.out","r") as f: 
    mraw = f.read()[:-1]
with open("/home/pi/esd_ece3186/logs/water_bool.out","r") as f: 
    lbool = f.read()[:-1]

if lbool == '1':
	string1 ="High"
else:
	string1 = "Low"

val_bme = []
with open("/home/pi/esd_ece3186/logs/bme.out","r") as f: 
    for line in f: 
        val_bme.append(line[:-1])

print(f'https://dweet.io/dweet/for/1b4859dd82e401fc0325e9134b6bac19ec4036bbace?wl={wstr}&wl_m={string1}&sm={mbool}&sm_v={mraw}&tm={val_bme[0]}&hm={val_bme[1]}')
r = requests.get(f'https://dweet.io/dweet/for/1b4859dd82e401fc0325e9134b6bac19ec4036bbace?wl={wstr}&wl_m={string1}&sm={mbool}&sm_v={mraw}&tm={val_bme[0]}&hm={val_bme[1]}')
print(r)
