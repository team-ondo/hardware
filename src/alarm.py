import time
from os import path
from pygame import mixer

ONDO_ANNOUNCER_HOT = path.join(path.dirname(__file__), "./audio/ondo_announcer_hot.wav")
ONDO_ANNOUNCER_COLD = path.join(path.dirname(__file__), "./audio/ondo_announcer_cold.wav")

def on_hot():
    mixer.init()
    alarm = mixer.Sound(ONDO_ANNOUNCER_HOT)
    alarm.play()

def on_cold():
    mixer.init()
    alarm = mixer.Sound(ONDO_ANNOUNCER_COLD)
    alarm.play()

def off():
    mixer.stop()

if __name__ == '__main__': 
    while True:
        on_cold();
        time.sleep(1)  
        off() 
        time.sleep(10)
    