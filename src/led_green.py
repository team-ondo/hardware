import RPi.GPIO as GPIO
from time import sleep

LED_GREEN = 25

#Set warnings off (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GREEN,GPIO.OUT)
    
def on():
    GPIO.output(LED_GREEN,GPIO.HIGH)

def off():
    GPIO.output(LED_GREEN,GPIO.LOW)

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