import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir = 16
GPIO.setup(pir, GPIO.IN)

print('Initializing Sensor...')

def getMotion():

    try:
        motion = GPIO.input(pir)
        if motion:
            # when motion detected
            return True
        
        elif not motion:
            # when motion not detected
            return False

    except KeyboardInterrupt:
        GPIO.cleanup() #reset GPIO

if __name__ == "__main__":
    print(getMotion())