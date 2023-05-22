#!/usr/bin/env python3
# import pprint

import requests

term = input("Please enter a topic for your jokes: ")

headers = {"User-Agent": "CS161 Demo parisj@linnbenton.edu", "Accept": "application/json"}
params = {"limit": 10, "term": term}
res = requests.get("https://icanhazdadjoke.com/search", headers=headers, params=params, timeout=1)

res.raise_for_status()

if res.ok:
    json_payload = res.json()
    number_of_jokes = json_payload["total_jokes"]

    if not number_of_jokes:
        print(f"Sorry, I guess {term} isn't very funny.\nNo jokes about it were found.")

    for index in range(number_of_jokes):
        print(f"joke {index + 1 } of {number_of_jokes}")
        print(f"{json_payload['results'][index]['joke']}")

    # print(json_payload["joke"])
    # pprint.pprint(json_payload, indent=4)
