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
    time.sleep(0.1)

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

servo_direction=range(120,500,30)
def find_paths(dict):
    lst=[]
    lst2=[]
    for way in servo_direction:
        if dict[way]>=25:
            lst.append(way)
            if len(lst)==5:
                return lst
            elif len(lst)==4 and (lst[0]==120 or lst[-1]==480):
                return lst
        else:
            lst=[]
    return lst2

def find_angle(lst_func):
    if len(lst_func)==0:
        return "back"
    if len(lst_func)==4 and lst_func[0]==120:
        return "right"
    elif len(lst_func)==4 and lst_func[-1]==480:
        return "left"
    elif (300-(sum(lst_func)/5))/2<0:
	return "left"
    elif (300-(sum(lst_func)/5))/2>0:
        return "right"
    return "back"

def check_obstacle():
#    servo_direction.reverse()
    sensor_values={}
    for dir in servo_direction:
        servo(dir)
        sensor_values[dir]=int(sensor())
    return sensor_values

M1=move_motor(1)
M2=move_motor(2)
def turn_car(direction):
   if direction=="right":
	M2.stop()
	M1.forward()
	time.sleep(0.5)
	M1.stop()
   if direction=="left":
        M1.stop()
        M2.forward()
        time.sleep(0.5)
        M2.stop()
   if direction=="back":
        M1.reverse()
        M2.reverse()
        time.sleep(0.5)
        M1.stop()
        M2.stop()


def main():
    servo(300)
    while True:
        if int(sensor())>=25:
            M1.forward()
            M2.forward()
        else:
            M1.stop()
            M2.stop()
            t_start=time.time()
            p=find_angle(find_paths(check_obstacle()))
            turn_car(p)
            servo(300)
        time.sleep(0.1)

if __name__=="__main__":
    main()
