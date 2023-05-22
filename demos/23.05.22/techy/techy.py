#!/usr/bin/env python3
import requests

res = requests.get("https://techy-api.vercel.app/api/json", timeout=1)

res.raise_for_status()

if res.ok:
    json_str = res.json()
    # print(res.text)
    print(json_str.keys())
    print(json_str)
