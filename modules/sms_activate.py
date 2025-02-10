# modules/sms_activate.py
import requests
import time
from config.config import Config

API_KEY = "34e07d1c68319cc253A9438eb196c37d"

def get_phone_number():
    url = f"https://sms-activate.ru/stubs/handler_api.php?api_key={API_KEY}&action=getNumber&service=go&country=0"
    response = requests.get(url)
    data = response.text.split(':')
    
    if data[0] != 'ACCESS_NUMBER':
        raise Exception(f"SMS-Activate error: {data[0]}")
    
    activation_id = data[1]
    phone_number = data[2]
    return activation_id, phone_number

def get_sms(activation_id):
    url = f"https://sms-activate.ru/stubs/handler_api.php?api_key={API_KEY}&action=getStatus&id={activation_id}"
    
    for _ in range(20):
        response = requests.get(url)
        if response.text.startswith('STATUS_OK'):
            return response.text.split(':')[1]
        time.sleep(5)
    
    raise Exception("Failed to receive SMS")
