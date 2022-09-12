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
# origins = [
#     f'{URL}',
#     f'{URL}/sensor_data'
# ]

# app.add_middleware(
#     CORSMiddleware, 
#     # TODO change origin 
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
#     )

class Device_Input(BaseModel):
    temperature_c: float
    temperature_f: float
    humidity: float
    motion: str
    alarm: str
    button: str

@app.post('/sensor_data')
async def send_data_post(device_input: Device_Input):
    return device_input

