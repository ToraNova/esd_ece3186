#!/usr/bin/python3
from i2c.lcd import lcd
from time import *

disp = lcd()

disp.lcd_display_string("Hello world", 1)
disp.lcd_display_string("My name is", 2)
disp.lcd_display_string("picorder", 3)
disp.lcd_display_string("I am a Raspberry Pi", 4)
