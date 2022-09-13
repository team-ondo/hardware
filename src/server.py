from ast import alias
from xmlrpc.client import boolean
import requests
import json
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


URL = 'http://127.0.0.1:8000'
DEVICE_ID = '1'

## RECEIVE DATA IN
app = FastAPI()
class Device_Input(BaseModel):
    temperature_c: float
    temperature_f: float
    humidity: float
    motion: str
    alarm: str
    button: str
    created_at: str

@app.post(f'/device-data/{DEVICE_ID}', response_model=Device_Input)
async def send_data_post(device_input: Device_Input):
    return device_input

