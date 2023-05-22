#!/usr/bin/env python3
import requests

# headers = {"Accept": "text/plain"}
headers = {"Accept": "application/json"}
params = {"language": "en"}
response = requests.get(
    "https://uselessfacts.jsph.pl/api/v2/facts/random", headers=headers, params=params, timeout=1
)

json_str = response.json()

# print(response.text)
print(f"id: {json_str['id']}")
print(f"random fact: {json_str['text']}")
