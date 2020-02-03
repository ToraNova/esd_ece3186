#!/usr/bin/python
from i2c import bme280

temperature,pressure,humidity = bme280.readBME280All()

with open("logs/bme.out", "w") as f: 
    f.write("%.1f\n%.1f\n" % (temperature,humidity))
    





