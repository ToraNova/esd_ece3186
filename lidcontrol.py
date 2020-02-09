#!/usr/bin/python3
import RPi.GPIO as gpio
import time
import requests

print("Lidcontrol started")

control_pins = [26,19,13,6]

gpio.setmode(gpio.BCM)
for pin in control_pins:
	gpio.setup(pin, gpio.OUT)
	gpio.output(pin, 0)

halfstep_seq_clockwise = [
    [1,0,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
    [0,0,0,1]]

halfstep_seq_anticlockwise = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]]

rbool = None
ldopn = False

def lidopen():
    gpio.setmode(gpio.BCM)
    for pin in control_pins:
            gpio.setup(pin, gpio.OUT)
            gpio.output(pin, 0)
    for i in range(128):
        for halfstep in range(8):
            for pin in range(4):
                gpio.output(control_pins[pin], halfstep_seq_clockwise[halfstep][pin])
            time.sleep(0.001)
    for pin in control_pins:
            gpio.output(pin, 0)
    gpio.cleanup()

def lidclose():
    gpio.setmode(gpio.BCM)
    for pin in control_pins:
            gpio.setup(pin, gpio.OUT)
            gpio.output(pin, 0)
    for i in range(128):
        for halfstep in range(8):
            for pin in range(4):
                gpio.output(control_pins[pin], halfstep_seq_anticlockwise[halfstep][pin])
            time.sleep(0.001)
    for pin in control_pins:
            gpio.output(pin, 0)
    gpio.cleanup()

ldstr = 'Closed'
rstr = "uninit"
try:
    while True:
        with open("/home/pi/esd_ece3186/logs/rain_bool.out","r") as f: 
            rbool = f.read()[:-1]

        if rbool == "1":
            rstr = "Raining !"
            if not ldopn:
                # raining and not open
                lidopen()
                ldstr = 'Opened'
                ldopn = True

        else :
            rstr = "Not Raining !"
            if ldopn:
                # not raining and open
                lidclose()
                ldstr = 'Closed'
                ldopn = False

        r = requests.get(f'https://dweet.io/dweet/for/1b4859dd82e401fc0325e9134b6bac19ec4036bbace?lid={ldstr}&rs={rstr}')
        #print(r)
        time.sleep(30)

except KeyboardInterrupt:
    gpio.cleanup()
    exit(0)
