#!/usr/bin/python3
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
control_pins = [26,19,13,6]

for pin in control_pins:
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, 0)

halfstep_seq = [
    [1,0,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
    [0,0,0,1]]

for i in range(512):
    for halfstep in range(8):
        for pin in range(4):
            gpio.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)

gpio.cleanup()
