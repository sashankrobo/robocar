import sys
import time
import getch
import RPi.GPIO as GPIO
import Adafruit_PCA9685
GPIO.setmode(GPIO.BOARD)
#mode=GPIO.getmode()
pwm = Adafruit_PCA9685.PCA9685()

Motor1A = 11
Motor1B = 12
Motor2A = 13
Motor2B = 15
TRIG = 16
ECHO = 18

GPIO.cleanup()
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)



def sensor():
#    TRIG = 16
#    ECHO = 18
#    print "Distance Measurement In Progress"
#    GPIO.setup(TRIG,GPIO.OUT)
#    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(0.05)
    GPIO.output(TRIG, True)
    time.sleep(0.000001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print "Distance:",distance,"cm"
#    GPIO.cleanup()
    if distance<25.0:
        return True
    else:
        return False

def servo(angle):
#    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)
    if angle==0:
        pwm.set_pwm(0, 0, 300)
        time.sleep(0.2)
    elif angle=="LFT1":
        pwm.set_pwm(0, 0, 400)
        time.sleep(0.2)
    elif angle=="LFT2":
        pwm.set_pwm(0, 0, 500)
        time.sleep(0.2)
    elif angle=="RHT1":
        pwm.set_pwm(0, 0, 220)
        time.sleep(0.2)
#        return "LFT"
    elif angle=="RHT2":
        pwm.set_pwm(0, 0, 120)
        time.sleep(0.2)
#        return "RHT" 
def forward():
    GPIO.output(Motor1A, True)
    GPIO.output(Motor1B, False)
    GPIO.output(Motor2A, True)
    GPIO.output(Motor2B, False)
    print("moving motor forward")
#    time.sleep(1)
#    GPIO.output(Motor1A, False)
#    GPIO.output(Motor2A, False)

def reverse():
    GPIO.output(Motor1A, False)
    GPIO.output(Motor1B, True)
    GPIO.output(Motor2A, False)
    GPIO.output(Motor2B, True)
    print("moving motor forward")
    time.sleep(2)
    GPIO.output(Motor1B, False)
    GPIO.output(Motor2B, False)


def turn(servo_angle):
    if servo_angle=="RHT":
        GPIO.output(Motor1A, False)
	GPIO.output(Motor1B, True)
	GPIO.output(Motor2A, True)
	GPIO.output(Motor2B, False)
	time.sleep(1)
        GPIO.output(Motor1B, False)
        GPIO.output(Motor2A, False)
        print("turning motors right")
    elif servo_angle=="LFT":
        GPIO.output(Motor1A, True)
	GPIO.output(Motor1B, False)
	GPIO.output(Motor2A, False)
	GPIO.output(Motor2B, True)
	time.sleep(1)
        GPIO.output(Motor1A, False)
        GPIO.output(Motor2B, False)
        print("turning motors left")
    elif servo_angle=="STOP":
        GPIO.output(Motor1A, False)
        GPIO.output(Motor1B, False)
        GPIO.output(Motor2A, False)
        GPIO.output(Motor2B, False)
        print("stopping motors")

while True:
#    IN=getch.getch()
#    p=input("Provide Distance:")
#    if IN=="x":
#        break
    if sensor()==False:
        servo(0)
        forward()
        time.sleep(0.1)
        continue
    if sensor()==True:
        turn("STOP")
        servo("LFT2")
        L2=sensor()
        servo("LFT1")
        L1=sensor()
        servo("RHT1")
        R1=sensor()
        servo("RHT1")
        R2=sensor()
        servo(0)
    if L1 or L2:
        if R1 or R2:
            reverse()
            turn("LFT")
        else:
            turn("RHT")
    else:
        turn("LFT")
