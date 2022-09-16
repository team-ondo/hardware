#!/bin/python

import adafruit_dht
import board
from time import sleep
from exception import CouldNotReadTempHumiditySensorRuntimeError, CouldNotReadTempHumiditySensorUnRecoverableError

# Initialize the dht device
dhtDevice = adafruit_dht.DHT22(board.D4)

def get_temp():
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (1.8) + 32
        humidity = dhtDevice.humidity
        
        temp_sensor_data = {
            'temperature_c': temperature_c,
            'temperature_f': temperature_f,
            'humidity': humidity
        }
        return temp_sensor_data

    except RuntimeError as e:
        raise CouldNotReadTempHumiditySensorRuntimeError(e)
    except Exception as e:
        dhtDevice.exit()
        raise CouldNotReadTempHumiditySensorUnRecoverableError(e)

if __name__ == "__main__":
    while True:
        print(get_temp())
        sleep(2)