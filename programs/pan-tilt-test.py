import Adafruit_PCA9685
import time
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
def servo1(angle):
#    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm(1, 0, angle)
    time.sleep(0.07)

def servo2(angle):
#    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm(2, 0, angle)
    time.sleep(0.07)

servo_direction=[x for x in range(120,500,30)]
def check_obstacle():
    servo_direction.reverse()
    sensor_values={}
    for dir in servo_direction:
        servo1(dir)
        servo2(dir)
        p=input("press enter:")
#        sensor_values[dir]=int(sensor())
    return sensor_values
for i in range(1,5):
    check_obstacle()
