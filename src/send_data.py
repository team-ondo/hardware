import requests
from requests import RequestException
from pprint import pprint
from time import sleep
# import os
# from dotenv import load_dotenv

# load_dotenv()

# URL = os.getenv("SERVER_URL")
# DEVICE_ID = '1'

def send_data(data, url, device_id):
    try:
        print('Sending')
        # pprint(data)
        res = requests.post(f'{url}/device-data/{device_id}', json = data)
        print(res.text)

        try:
            res.raise_for_status()
            
        except RequestException as e:
            print("Request failed: ", e)
            pass

        print('Successfully send the data to server')

    except Exception as e:
        print("Some failure occurred when monitoring sensor", e)

if __name__ == '__main__': 
    while True:
        send_data({
            "temperature_c": 90.6,
            "temperature_f": 0.5,
            "humidity": 45.0,
            "motion": "MOTION",
            "alarm": "ALARM",
            "button_home": "BH",
            "created_at": "some date and time"
        }, "http://127.0.0.1:8000", 1)
        sleep(2)
