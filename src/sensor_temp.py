#!/bin/python

import adafruit_dht
import board
import time

# Initialize the dht device
dhtDevice = adafruit_dht.DHT22(board.D4)

def getTemp():
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

    except RuntimeError as error:
        return error.args[0]
    except Exception as error:
        # TODO: Send error info to the database
        dhtDevice.exit()
        raise error
