#!/usr/bin/python
# cannot use python3 because smbus not working there
# Modified script from https://github.com/JasperWallace/chirp-graphite/blob/master/chirp.py
# by DanielTamm

import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 1

while True:

	moisture = adc.read_adc(1, gain=GAIN)
	with open("logs/moisture_value.out", "w") as f: 
			f.write("%f\n" %(moisture))

	print ("Moisture: ", moisture)

	time.sleep(0.5)