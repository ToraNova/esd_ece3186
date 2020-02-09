#!/usr/bin/python3
import requests

val_wl = []
with open("/home/pi/esd_ece3186/logs/waterlevel_value.out","r") as f1: 
    for line in f1: 
        val_wl.append(line)

r = requests.get(f'https://dweet.io/dweet/for/1b4859dd82e401fc0325e9134b6bac19ec4036bbace8ec7b6906f47ac4b1ed13?wl={val_wl[0]}&foo=bar')
print(r)
