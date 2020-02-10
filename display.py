#!/usr/bin/python3
# LCD Display script
# using the i2c I/O expander module along with the lcd display library
# read from bme.out and moist_bool.out to display on the 2 row LCD screen
from i2c.lcd import lcd
from time import *

disp = lcd()
#disp.lcd_display_string("Hello world", 1)
#disp.lcd_display_string("My name is", 2)

val = []
with open("/home/pi/esd_ece3186/logs/bme.out","r") as f:
    for line in f:
        val.append(line[:-1])

mbool = None
with open("/home/pi/esd_ece3186/logs/moist_bool.out","r") as f:
    mbool = f.read()[:-1]

disp.lcd_display_string("T:%sC  H:%s" % (val[0],val[1]), 1)
disp.lcd_display_string("SoilMoisture:%s" % (mbool), 2)
#print ("%s"%(val1[0]))
