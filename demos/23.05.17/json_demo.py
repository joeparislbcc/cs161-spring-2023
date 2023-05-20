#!/usr/bin/env python3
"""https://jsonplaceholder.typicode.com/
https://dummyjson.com/"""
import json

import requests  # pip install requests

response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=1)

if response.ok:
    # users = response.json()
    users = json.dumps(response.json(), indent=2)

    # print(users)
    # print(json.dumps(users, indent=2))
    print(users)
    # print(json.dumps(users[0], indent=2))
    # print(type(users[0]["completed"]))
    # print(users[0].keys())

    with open("users.json", mode="w", encoding="utf-8") as outfile:
        outfile.write(users)
