#!/usr/bin/python3
import RPi.GPIO as gpio
import time
# Pins for Motor Driver Inputs 
Motor1A = 11
Motor1B = 12
Motor2A = 13
Motor2B = 15

gpio.setmode(gpio.BOARD)

gpio.setup(Motor1A, gpio.OUT)
gpio.setup(Motor1B, gpio.OUT)
gpio.setup(Motor2A, gpio.OUT)
gpio.setup(Motor2B, gpio.OUT)

gpio.output(Motor1A, True)
gpio.output(Motor1B, False)
gpio.output(Motor2A, False)
gpio.output(Motor2B, True)
time.sleep(.5)

gpio.cleanup()
