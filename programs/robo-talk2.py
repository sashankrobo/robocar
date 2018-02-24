#!/usr/bin/python
from gtts import gTTS
import os
import time
def main():
#    tts=gTTS(text="helllo sashank!!! i am Robo. Please talk to me. Today, i want to tell you a story. It's name is Sly Fox", lang='en')
#    tts.save("audios/first.mp3")
#    os.system("omxplayer audios/first.mp3")
#    time.sleep(2)
#    tts=gTTS(text="helllo sashank!!!Are you hearing?",lang='en')
#    tts.save("audios/wakeup.mp3")
    lst=os.listdir("stories")
    sorted_lst=sorted(lst)
    n=0
    for p in sorted_lst:
	print(p)
        os.system("omxplayer --no-osd stories/{}".format(p))
	time.sleep(2)
	n+=1
	if n==5:
	    os.system("omxplayer --no-osd audios/wakeup.mp3")
	    print("{} spoken".format(p))
if __name__=="__main__":
    main()
