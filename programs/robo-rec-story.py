#!/usr/bin/python
import os
from gtts import gTTS
sent_list=[]
sent=[]
with open("fox.txt","r") as f:
    for i in f:
	for j in list(i.strip()):
	    if j!=".":
		sent.append(j)
	    else:
		sent.append(".")
		sent_list.append("".join(sent))
		sent=[]
#print(sent_list)
k=0
for i in sent_list:
    tts=gTTS(text=i,lang='en-us')
    tts.save("stories/fox_sentense_{}.mp3".format(k))
    k+=1
