#!/usr/bin/python3
import RPi.GPIO as gpio
import time

ledpin = 4
gpio.setmode(gpio.BCM)
gpio.setup(ledpin, gpio.OUT)
gpio.output(ledpin ,1)
time.sleep(1)
gpio.output(ledpin ,0)
gpio.cleanup()
