#!/usr/bin/python
from gtts import gTTS
import os
#def main():
tts=gTTS(text="""You have chosen to move the car...
....Please instruct me.....
....Options are ...forward, reverse, left, right, stop.....""", lang='en-us')
tts.save("audios/carmoveoptions.mp3")
#    os.system("omxplayer audios/first.mp3")
#    with open ("stories/fox.txt","r") as f:
#	for line in f:
#	    print(line)
#	    print("=====")
#if __name__=="__main__":
#    main()
