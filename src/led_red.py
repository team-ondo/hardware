import RPi.GPIO as GPIO
from time import sleep

LED_RED = 24

#Set warnings off (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED,GPIO.OUT)
    
def on():
    GPIO.output(LED_RED,GPIO.HIGH)

def off():
    GPIO.output(LED_RED,GPIO.LOW)

def blink():
    on()
    sleep(0.3)
    off()
    sleep(0.3)

if __name__ == '__main__':
    try:
        while True:
            blink()
    except KeyboardInterrupt:
        GPIO.cleanup()