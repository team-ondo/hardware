import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir = 16
GPIO.setup(pir, GPIO.IN)

print('Initializing Sensor...')
sleep(2) # allow sensor time to intialize
print("Let's do this")

def getMotion():

    try:
        motion = GPIO.input(pir)
        if motion:
            # print("MOTION DETECTED")
            return True
        
        elif not motion:
            # print("<no motion>")
            return False

    except KeyboardInterrupt:
        GPIO.cleanup() #reset GPIO

while True:
    print(getMotion())
    sleep(2)