#!/usr/bin/env python3
import requests  # pip install requests

response = requests.get("https://google.com", timeout=1)

if response.status_code == 200:
    print(response.text)
