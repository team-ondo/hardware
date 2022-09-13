from ast import alias
from venv import create
from xmlrpc.client import boolean
from sensor_temp import getTemp
from sensor_motion import getMotion 
from alarm import alarm_on
from button import button_pressed
import requests
import json
import time
import datetime

URL = 'http://127.0.0.1:8000'
DEVICE_ID = '1'

## SEND DATA OUT   
def create_sensor_data_dict():
    
    try:
        sensor_temp = getTemp()
        temp_c = round(sensor_temp["temperature_c"], 1)
        temp_f = round(sensor_temp["temperature_f"], 1)
        humidity = sensor_temp["humidity"]
        motion = getMotion()
        alarm = alarm_on()
        button = button_pressed()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return {
            'temperature_c': temp_c,
            'temperature_f': temp_f,
            'humidity': humidity,
            'motion': motion,
            'alarm': alarm,
            'button': button,
            'created_at': timestamp
        }

    except:
        return sensor_temp

## LOOP DATA SEND OUT
# ignore this code block on import as module
if __name__ == '__main__': 
    while True:
        result = create_sensor_data_dict()
        if type(result) == dict:
            req = requests.post(f'{URL}/device-data/{DEVICE_ID}', json = result)
            print(req.text)
        time.sleep(2)