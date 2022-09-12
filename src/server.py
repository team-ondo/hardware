from ast import alias
from xmlrpc.client import boolean
import requests
import json
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


URL = 'http://127.0.0.1:8000'

## RECEIVE DATA IN

app = FastAPI()

@app.get('/')
async def root():
    return {'message': "Hello World"}

class Device_Input(BaseModel):
    temperature_c: float
    temperature_f: float
    humidity: float
    motion: str
    alarm: str
    button: str

@app.post('/sensor_data')
async def send_data_post(device_input: Device_Input):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(device_input)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    return device_input

