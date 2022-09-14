from http.client import TOO_MANY_REQUESTS
from itertools import count
from alarm import alarm_on
from button import button_input
from sensor_temp import getTemp
from time import sleep

TOO_HOT = 26.2
DELAY_COUNTER = 50

sound_the_alaram = False
button_was_pressed = False
counter = 0

while True:
    print(counter)
    try:
        temperature_c = getTemp()["temperature_c"]
        print(temperature_c)

        if temperature_c > TOO_HOT and counter % DELAY_COUNTER == 0:
            print("Sound the alarm!")
            sound_the_alaram = True
            counter = 0

        if button_input():
            button_was_pressed = True

        if sound_the_alaram and not button_was_pressed:
            alarm_on()
            sound_the_alaram = False
            button_was_pressed = False

        counter += 1

    except:
        print("failed")

    sleep(0.1) 

