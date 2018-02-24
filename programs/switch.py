import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN)
prev_input=0
while True:
    input=GPIO.input(29)
    if (input):
        print("Button pressed")
        prev_input=input
        time.sleep(0.5)
