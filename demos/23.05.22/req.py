#!/usr/bin/env python3
import requests  # pip install requests

response = requests.get("https://google.com", timeout=1)

# get - give me
# post - create new
# put - insert, replace if already exists
# patch - update, modify
# delete - delete

response.raise_for_status()  # raise an exception on 400- or 500-level status code

# if response.status_code == 200:
if response.ok:
    print(response.text)
