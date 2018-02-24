import os
import menu
import carmove
moveoptions=["forward","backward","left","right","stop","exit"]
option1=["1","move car","move","car"]
def option(text):
    for attem in range(3):
        if text in option1:
            os.system("omxplayer audios/carmoveoptions.mp3")
            while True:
                movetext=menu.listen()
                if movetext in moveoptions:
                    if movetext=="exit":
                        break
                    elif movetext=="forward":
                        carmove.forward()
                        carmove.stop()
                    elif movetext=="backward":
                        carmove.reverse()
                        carmove.stop()
                    elif movetext=="left":
                        carmove.left()
                        carmove.stop()
                    elif movetext=="right":
                        carmove.right()
                        carmove.stop()
                    elif movetext=="stop":
                        carmove.stop()

        else:
            if attem==2:
                print("No options selected. Good bye")
            os.system("omxplayer audios/reattempt.mp3")
