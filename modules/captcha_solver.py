# modules/captcha_solver.py
import requests
import time
from config.config import Config

API_KEY = "69ee89ee24e45c7a72220524f3ef1ad0"

def solve_captcha(captcha_base64):
    url = "http://2captcha.com/in.php"
    data = {
        'key': API_KEY,
        'method': 'base64',
        'body': captcha_base64,
        'json': 1
    }
    response = requests.post(url, data=data)
    request_id = response.json().get('request')
    
    if response.json().get('status') != 1:
        raise Exception(f"2Captcha error: {response.json().get('request')}")
    
    result_url = f"http://2captcha.com/res.php?key={API_KEY}&action=get&id={request_id}&json=1"
    
    for _ in range(20):
        result_response = requests.get(result_url)
        if result_response.json().get('status') == 1:
            return result_response.json().get('request')
        time.sleep(5)
    
    raise Exception("Failed to solve CAPTCHA")
