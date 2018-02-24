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
#    print "Waiting For Sensor To Settle"
#    time.sleep(0.05)
    GPIO.output(TRIG, True)
    time.sleep(0.000005)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
#    print "Distance:",distance,"cm"
#    GPIO.cleanup()
    if distance<20.0:
        print "Distance:",distance,"cm"
        return 1
    else:
        return 0

pwm.set_pwm_freq(50)
def servo(angle):
#    pwm = Adafruit_PCA9685.PCA9685()
    if angle=="STR":
        pwm.set_pwm(0, 0, 300)
#        time.sleep(0.4)
    elif angle=="LFT1":
        pwm.set_pwm(0, 0, 370)
#        time.sleep(0.4)
    elif angle=="LFT2":
        pwm.set_pwm(0, 0, 440)
#        time.sleep(0.4)
    elif angle=="RHT1":
        pwm.set_pwm(0, 0, 220)
#        time.sleep(0.4)
#        return "LFT"
    elif angle=="RHT2":
        pwm.set_pwm(0, 0, 150)
#        time.sleep(0.4)
#        return "RHT"
def move_motor(motor_no,direction):
    motorA="Motor{}A".format(motor_no)
    motorB="Motor{}B".format(motor_no)
    if direction is "forward":
        GPIO.output(MotorA, True)
        GPIO.output(MotorB, False)
    elif direction is "reverse":
        GPIO.output(MotorA, False)
        GPIO.output(MotorB, True)
    elif direction is "stop":
        GPIO.output(MotorA, False)
        GPIO.output(MotorB, False)
#    time.sleep(1)
#    GPIO.output(Motor1A, False)
#    GPIO.output(Motor2A, False)

def reverse():
    GPIO.output(Motor1A, False)
    GPIO.output(Motor1B, True)
    GPIO.output(Motor2A, False)
    GPIO.output(Motor2B, True)
#    print("moving motor forward")
    time.sleep(0.5)
    GPIO.output(Motor1B, False)
    GPIO.output(Motor2B, False)


def move(servo_angle):
    if servo_angle=="RHT1":
        GPIO.output(Motor1A, False)
        GPIO.output(Motor1B, True)
        GPIO.output(Motor2A, True)
        GPIO.output(Motor2B, False)
        time.sleep(0.6)
        GPIO.output(Motor1B, False)
        GPIO.output(Motor2A, False)
#        print("turning motors RHT1")
    elif servo_angle=="LFT1":
        GPIO.output(Motor1A, True)
        GPIO.output(Motor1B, False)
        GPIO.output(Motor2A, False)
        GPIO.output(Motor2B, True)
        time.sleep(0.6)
        GPIO.output(Motor1A, False)
        GPIO.output(Motor2B, False)
#        print("turning motors LFT1")
    elif servo_angle=="STOP":
        GPIO.output(Motor1A, False)
        GPIO.output(Motor1B, False)
        GPIO.output(Motor2A, False)
        GPIO.output(Motor2B, False)
#        print("stopping motors")
    elif servo_angle=="RHT2":
        GPIO.output(Motor1A, False)
        GPIO.output(Motor1B, True)
        GPIO.output(Motor2A, True)
        GPIO.output(Motor2B, False)
        time.sleep(1)
        GPIO.output(Motor1B, False)
        GPIO.output(Motor2A, False)
#       print("turning motors RHT2")
    elif servo_angle=="LFT2":
        GPIO.output(Motor1A, True)
        GPIO.output(Motor1B, False)
        GPIO.output(Motor2A, False)
        GPIO.output(Motor2B, True)
        time.sleep(1)
        GPIO.output(Motor1A, False)
        GPIO.output(Motor2B, False)
#        print("turning motors LFT2")
    elif servo_angle=="STR":
        GPIO.output(Motor1A, True)
        GPIO.output(Motor1B, False)
        GPIO.output(Motor2A, True)
        GPIO.output(Motor2B, False)
#        print("moving motor forward")
servo_direction=["LFT2","LFT1","STR","RHT1","RHT2"]
def check_obstacle():
    servo_direction.reverse()
#    servo(0)
    sensor_values={}
    for dir in servo_direction:
        servo(dir)
        time.sleep(0.5)
        sensor_values[dir]=int(sensor())
#    servo("STR")
    return sensor_values

while True:
#    servo_direction=["LFT2","LFT1","STR","RHT1","RHT2"]
    mal=check_obstacle()
    for Key,val in mal.items():
#        servo(dir)
#	time.sleep(0.2)
	if Key=="STR" and val:
	    move("STOP")
	    reverse()
	    time.sleep(0.5)
#	    move("LFT1")
	    continue
	elif (Key=="LFT2" and val)or (Key=="LFT1" and val):
	    move("RHT1")
	    time.sleep(0.5)
	    continue
	elif (Key=="RHT2" and val) or (Key=="RHT1" and val):
	    move("LFT1")
	    time.sleep(0.5)
	    continue
	if Key=="STR" and not val:
	    move("STR")
#    time.sleep(0.2)

