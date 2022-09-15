import RPi.GPIO as GPIO
from time import sleep

BUTTON_ALARM = 23
ON = 0

#Set warnings off (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_ALARM,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def pushed():
    button_state = GPIO.input(BUTTON_ALARM)
    if button_state == ON:
        return True
    else:
        return False

if __name__ == '__main__': 
    while True:
        print(pushed())
        sleep(0.5)
