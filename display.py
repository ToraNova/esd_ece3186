#!/usr/bin/python3
from i2c.lcd import lcd
from time import *

disp = lcd()
#disp.lcd_display_string("Hello world", 1)
#disp.lcd_display_string("My name is", 2)

val = []
with open("logs/bme.out","r") as f: 
    for line in f: 
        val.append(line[:-1])

disp.lcd_display_string("T:%sC  H:%s" % (val[0],val[1]), 1)
