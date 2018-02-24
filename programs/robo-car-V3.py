import sys
import time
import getch
import RPi.GPIO as GPIO
import Adafruit_PCA9685
GPIO.setmode(GPIO.BOARD)
#mode=GPIO.getmode()
pwm = Adafruit_PCA9685.PCA9685()

#Motor1A = 11
#Motor1B = 12
#Motor2A = 13
#Motor2B = 15
#TRIG = 16
#ECHO = 18

pin_dict={"Motor1A":11,"Motor1B":12,"Motor2A":13,"Motor2B":15,"TRIG":16,"ECHO":18}
GPIO.cleanup()
GPIO.setup(pin_dict["Motor1A"], GPIO.OUT)
GPIO.setup(pin_dict["Motor1B"], GPIO.OUT)
GPIO.setup(pin_dict["Motor2A"], GPIO.OUT)
GPIO.setup(pin_dict["Motor2B"], GPIO.OUT)
GPIO.setup(pin_dict["TRIG"],GPIO.OUT)
GPIO.setup(pin_dict["ECHO"],GPIO.IN)


def sensor():
    GPIO.output(pin_dict["TRIG"], False)
    GPIO.output(pin_dict["TRIG"], True)
    time.sleep(0.000001)
    GPIO.output(pin_dict["TRIG"], False)
    pulse_start = time.time()
    while GPIO.input(pin_dict["ECHO"])==0:
        pulse_start = time.time()
    pulse_end = time.time()
    while GPIO.input(pin_dict["ECHO"])==1 and ((time.time()-pulse_start)*1000<5.0):
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
#    print("sense duration",pulse_duration*1000)
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

pwm.set_pwm_freq(50)
def servo(angle):
#    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm(0, 0, angle)
    time.sleep(0.07)

class move_motor():
    def __init__(self,motor_no):
        self.motor_no=motor_no
        self.Motor_A="self.Motor{}A".format(self.motor_no)
        self.Motor_B="self.Motor{}B".format(self.motor_no)
    def reverse(self):
        GPIO.output(pin_dict["Motor{}A".format(self.motor_no)],True)
        GPIO.output(pin_dict["Motor{}B".format(self.motor_no)], False)
    def forward(self):
        GPIO.output(pin_dict["Motor{}A".format(self.motor_no)],False)
        GPIO.output(pin_dict["Motor{}B".format(self.motor_no)], True)
    def stop(self):
        GPIO.output(pin_dict["Motor{}A".format(self.motor_no)],False)
        GPIO.output(pin_dict["Motor{}B".format(self.motor_no)], False)
	
servo_direction=[x for x in range(90,510,30)]
def check_obstacle():
    servo_direction.reverse()
    sensor_values={}
    for dir in servo_direction:
        servo(dir)
        sensor_values[dir]=int(sensor())
    return sensor_values

M1=move_motor(1)
M2=move_motor(2)
while True:
    t_start=time.time()
    mal=check_obstacle()
    for Key,val in mal.items():
        print("key:",Key,"value",val)
    t_stop=time.time()
    print("time taken:",t_stop-t_start)
    print("==================================")
    M1.forward()
#    M2.forward()
    time.sleep(1)
#    M2.stop()
    M1.stop()
    time.sleep(2)
 
