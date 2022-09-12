import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir = 16
GPIO.setup(pir, GPIO.IN)

print('Initializing Sensor...')
sleep(2)

def getMotion():
    if GPIO.input(pir):
        # motion detected
        return True
    
    elif not GPIO.input(pir):
        # no motion detected
        return False

    elif KeyboardInterrupt: 
        GPIO.cleanup() # reset GPIO
        print("Program ended")
