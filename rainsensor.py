#!/usr/bin/python3
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 1
threshold = 30000

rain_value = adc.read_adc(0, gain=GAIN)

if rain_value < threshold:
    #print ("Raining! ")
    rainbool = "1\n"
else:
    #print ("Not Raining!")
    rainbool = "0\n"

print(rain_value)
with open("/home/pi/esd_ece3186/logs/rain_bool.out", "w") as f: 
    f.write(rainbool)
