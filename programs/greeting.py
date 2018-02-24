import time
import os
def greeting_deco(obj):
    def wrapper():
        obj()
        os.system("omxplayer audios/greeting.mp3")
    return wrapper
@greeting_deco
def greet():
    currentTime=int(time.strftime('%H'))
    print(currentTime)
    if currentTime > 18:
        os.system("omxplayer audios/goodevening.mp3")    
    elif currentTime > 12:
        os.system("omxplayer audios/goodafternoon.mp3")    
    elif currentTime < 12:
        os.system("omxplayer audios/goodmorning.mp3")    
