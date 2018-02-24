#!/usr/bin/python3
###
###
import RPi.GPIO as gpio
import time
Motor1A = 11
Motor1B = 12
Motor2A = 13
Motor2B = 15
def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(Motor1A, gpio.OUT)
    gpio.setup(Motor1B, gpio.OUT)
    gpio.setup(Motor2A, gpio.OUT)
    gpio.setup(Motor2B, gpio.OUT)
    gpio.setup(29, gpio.IN)
setup()
def forward():
    gpio.output(Motor1A, True)
    gpio.output(Motor1B, False)
    gpio.output(Motor2A, True)
    gpio.output(Motor2B, False)
    time.sleep(1.5)
#    gpio.cleanup()
def reverse():
    gpio.output(Motor1A, False)
    gpio.output(Motor1B, True)
    gpio.output(Motor2A, False)
    gpio.output(Motor2B, True)
    time.sleep(1.5)
#    gpio.cleanup()
def left():
    gpio.output(Motor1A, False)
    gpio.output(Motor1B, True)
    gpio.output(Motor2A, True)
    gpio.output(Motor2B, False)
    time.sleep(.5)
#    gpio.cleanup()
def right():
    gpio.output(Motor1A, True)
    gpio.output(Motor1B, False)
    gpio.output(Motor2A, False)
    gpio.output(Motor2B, True)
    time.sleep(.5)
#    gpio.cleanup()
def stop():
    gpio.output(Motor1A, False)
    gpio.output(Motor1B, False)
    gpio.output(Motor2A, False)
    gpio.output(Motor2B, False)
#    time.sleep(.5)
