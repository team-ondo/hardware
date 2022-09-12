from ast import alias
from xmlrpc.client import boolean
from sensor_temp import getTemp
from sensor_motion import getMotion 
from alarm import alarm_on
from button import button_pressed
import requests
import json
import time


URL = 'http://127.0.0.1:8000'

## SEND DATA OUT

valid_data = {}

def create_sensor_data_dict():
    try:
        sensor_temp = getTemp()
        temp_c = round(sensor_temp["temperature_c"], 1)
        temp_f = round(sensor_temp["temperature_f"], 1)
        humidity = sensor_temp["humidity"]
        motion = getMotion()
        alarm = alarm_on()
        button = button_pressed()

        sensor_data_out = {
            'temperature_c': temp_c,
            'temperature_f': temp_f,
            'humidity': humidity,
            'motion': motion,
            'alarm': alarm,
            'button': button
        }

        valid_data = sensor_data_out
        return sensor_data_out
    except:
        # pass
        return valid_data

## LOOP DATA SEND OUT

while True:
    # create_sensor_data_dict()
    req = requests.post(f'{URL}/sensor_data', json = create_sensor_data_dict())
    print(req.text)
    time.sleep(2)