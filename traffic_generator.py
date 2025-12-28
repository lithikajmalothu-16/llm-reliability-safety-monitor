import requests
import time
import random

URL = "http://127.0.0.1:8000/ask"

payloads = [
    {"text": "Explain AI briefly"},
    {"text": "Write a detailed essay on quantum physics" * 20},
    {"text": "123 abc !!! ??? random test input"}
]

while True:
    payload = random.choice(payloads)
    try:
        requests.post(URL, json=payload, timeout=120)
    except Exception as e:
        print("Request failed:", e)
    time.sleep(3)
