import speech
import os
text=None
def speak():
    os.system("omxplayer audios/menu.mp3")
def listen():
    for attempt in range(3):
        text=speech.recognise()
        if not text:
            os.system("omxplayer audios/reattempt.mp3")
        else:
            return text
