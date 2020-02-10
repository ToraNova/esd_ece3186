#!/usr/bin/python
# this script uses the bme280 script to read from the bme280
# temp and humid sensor and outputs it to a file
from i2c import bme280

temperature,pressure,humidity = bme280.readBME280All()

with open("/home/pi/esd_ece3186/logs/bme.out", "w") as f:
    f.write("%.1f\n%.1f\n" % (temperature,humidity))






