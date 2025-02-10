# config/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    CAPTCHA_API_KEY = os.getenv("CAPTCHA_API_KEY")
    SMS_API_KEY = os.getenv("SMS_API_KEY")
    PROXY_USER = os.getenv("PROXY_USER")
    PROXY_PASS = os.getenv("PROXY_PASS")
    PROXY_DOMAIN = os.getenv("PROXY_DOMAIN")
    PROXY_PORT = os.getenv("PROXY_PORT")
