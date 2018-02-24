#!/usr/bin/env python3
import time
import Adafruit_PCA9685
import greeting
import gpiosetup
import menu
import chooseoptions
def main():
    gpiosetup.setup()
    while True:
        input=gpiosetup.gpio.input(29)
        if (input):
            print("Button pressed")
            time.sleep(0.5)
            greeting.greet()
            menu.speak()
            listen=menu.listen()
            chooseoptions.option(listen)

if __name__=="__main__":
    main()
