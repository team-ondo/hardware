#!/bin/python

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import adafruit_dht
import board
import time

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

def getTemp():
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        
        temp_sensor_data = {
            'temperature_c': temperature_c,
            'temperature_f': temperature_f,
            'humidity': humidity
        }

        # print(
        #     "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
        #         temperature_f, temperature_c, humidity
        #     )
        # )
        # return(
        #     "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
        #         temperature_f, temperature_c, humidity
        #     )
        # )
        return temp_sensor_data

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        # TODO if error happens continue. fetch the data after 1 or 2 seconds
        # print(error.args[0])
        return error.args[0]
    except Exception as error:
        # TODO: Send error info to the server
        dhtDevice.exit()
        raise error

# while True:
#     getTemp()
#     time.sleep(2)
