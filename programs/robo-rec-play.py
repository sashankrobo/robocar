#!/usr/bin/python
from gtts import gTTS
import os
def main():
#    tts=gTTS(text="helllo sashank!!! i am Robo. Please talk to me. you know one thing? 1 + 1 is 2", lang='en')
#    tts.save("audios/first.mp3")
    os.system("omxplayer test.wav")
if __name__=="__main__":
    main()
