import RPi.GPIO as gpio
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
