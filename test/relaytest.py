#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

pin = 5

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.LOW) 

time.sleep(2)

GPIO.output(pin, GPIO.HIGH)

time.sleep(2)

GPIO.cleanup()
