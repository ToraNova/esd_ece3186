#!/usr/bin/python
# cannot use python3 because smbus not working there
# Modified script from https://github.com/JasperWallace/chirp-graphite/blob/master/chirp.py
# by DanielTamm

import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 1

while True:

	water_level = adc.read_adc(2, gain=GAIN)

	time.sleep(1)
