import RPi.GPIO as GPIO
from time import sleep
from exception import CouldNotReadMotionSensorError

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR = 16
GPIO.setup(PIR, GPIO.IN)

print('Initializing Sensor...')

def get_motion():
    try:
        motion = GPIO.input(PIR)
        if motion:
            # when motion detected
            return True
        
        elif not motion:
            # when motion not detected
            return False

    except Exception as e:
        raise CouldNotReadMotionSensorError("Motion Sensor Error : ", e)

if __name__ == "__main__":
    while True:
        print(get_motion())
        sleep(.2)