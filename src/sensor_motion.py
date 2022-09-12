import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir = 16
GPIO.setup(pir, GPIO.IN)

print('Initializing Sensor...')
sleep(2)
print("Let's do this")

def getMotion():
    if GPIO.input(pir):
        # print("MOTION DETECTED")
        return True
    
    elif not GPIO.input(pir):
        # print("<no motion>")
        return False

    elif KeyboardInterrupt: 
        GPIO.cleanup() #reset GPIO
        print("Program ended")

# while True:
#     getMotion()
#     sleep(.2)
