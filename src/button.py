import RPi.GPIO as GPIO
from time import sleep

#Set warnings off (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set Button and LED pins
BUTTON = 23
LED = 24
#Setup BUTTON and LED
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

    
def button_input():
    button_state = GPIO.input(BUTTON)
    if button_state == 0:
        GPIO.output(LED,GPIO.HIGH)
        return True
    else:
        GPIO.output(LED,GPIO.LOW)
        return False


if __name__ == '__main__': 
    while True:
        print(button_input())
        sleep(0.5)