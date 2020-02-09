#!/usr/bin/python3
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
GAIN = 1

moisture = adc.read_adc(1, gain=GAIN)

if moisture>11000:
    boolstr = "Yes\n"
else:
    boolstr = "No\n"

with open("/home/pi/esd_ece3186/logs/moist_bool.out", "w") as f: 
    f.write(boolstr)

with open("/home/pi/esd_ece3186/logs/moist_raw.out", "w") as f: 
    f.write("%f\n" %(moisture))
