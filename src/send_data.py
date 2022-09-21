import requests
from requests import RequestException
from pprint import pprint
from time import sleep

def send_data(data, url, device_id):
    
    try:
        print('Sending')
        # pprint(data)
        res = requests.post(f'{url}/device-data/{device_id}', json = data)
        print(res.text)

        try:
            res.raise_for_status()
            return res.status_code
            
        except RequestException as e:
            print("Request failed: ", e)
            return res.status_code

        # print('Successfully send the data to server')

    except Exception as e:
        print("Some failure occurred when monitoring sensor", e)

def send_alarm(data, url, device_id):
    
    try:
        print('Sending')
        # pprint(data)
        res = requests.post(f'{url}/device/{device_id}/alarm/on', json = data)
        print(res.text)

        # {"text": "It's too hot in the room! Please check on your loved one"}

        try:
            res.raise_for_status()
            return res.status_code
            
        except RequestException as e:
            print("Request failed: ", e)
            return res.status_code

        # print('Successfully send the data to server')

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
