#!/usr/bin/python3
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 1

water_level = adc.read_adc(2, gain=GAIN)

# level % thresholding
if water_level<20800:
    lvlstring = "0\n"
elif water_level>20800 and water_level<21300:
    lvlstring = "25\n"
elif water_level>21300 and water_level<24000:
    lvlstring = "50\n"
elif water_level>24000 and water_level<25700:
    lvlstring = "75\n"
else:
    lvlstring = "100\n"

if water_level<15000:
    lvlbool = "0\n"
else:
    lvlbool = "1\n"

with open("/home/pi/esd_ece3186/logs/water_percent.out", "w") as f: 
    f.write(lvlstring)

with open("/home/pi/esd_ece3186/logs/water_bool.out", "w") as f: 
    f.write(lvlbool)

#print ("Water Level:", water_level)
