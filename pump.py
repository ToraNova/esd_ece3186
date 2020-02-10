#!/usr/bin/python3
# this script checks if there is water and if the soil is moist
# if conditions are met, it then fires the relay thus causing the
# pump to run and watering the soil
import RPi.GPIO as GPIO
import time

pin = 5

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

wbool = None
with open("/home/pi/esd_ece3186/logs/water_bool.out","r") as f:
    wbool = f.read()[:-1]

mbool = None
with open("/home/pi/esd_ece3186/logs/moist_bool.out","r") as f:
    mbool = f.read()[:-1]

if mbool == "No" and wbool == '1':
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(2)
else:
    pass

GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()
