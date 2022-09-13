from pygame import mixer
import time

def alarm_on():
    mixer.init()
    alarm = mixer.Sound('./audio/ondo_announcer.wav')
    alarm.play() 

if __name__ == '__main__': 
    while True:
        alarm_on();
        time.sleep(8)    
    

