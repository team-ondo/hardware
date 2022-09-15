from sensor_temp import getTemp
from sensor_motion import getMotion
from alarm import alarm_on
from button import button_pressed
import requests
from pprint import pprint
from requests import RequestException
import time
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("SERVER_URL")
DEVICE_ID = '1'

## SEND DATA OUT
def create_sensor_data_dict():
    """Create data from multiple sensors

    Raises:
        e: Failed to get data from sensor

    Returns:
        dict: Dictionary of sensor data
    """
    
    try:
        sensor_temp = getTemp()
        temp_c = round(sensor_temp["temperature_c"], 1)
        temp_f = round(sensor_temp["temperature_f"], 1)
        humidity = sensor_temp["humidity"]
        motion = getMotion()
        alarm = False #alarm_on()
        button = button_pressed()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return [{
            'temperature_c': temp_c,
            'temperature_f': temp_f,
            'humidity': humidity,
            'motion': motion,
            'alarm': alarm,
            'button': button,
            'created_at': timestamp
        }]

    except Exception as e:
        raise e

## LOOP DATA SEND OUT
# ignore this code block on import as module
if __name__ == '__main__': 
    while True:
        try:
            result = create_sensor_data_dict()
            print('##########')
            print('Sending')
            pprint(result)
            res = requests.post(f'{URL}/device-data/{DEVICE_ID}', json = result)
            try:
                res.raise_for_status()
            except RequestException as e:
                print("Request failed: ", e)
                continue

            print('Successfully send the data to server')
            time.sleep(5)
        except Exception as e:
            print("Some failure occurred when monitoring sensor")
