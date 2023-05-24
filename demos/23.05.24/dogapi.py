#!/usr/bin/env python3
import os
import pprint
import sys

import climage
import requests
from dotenv import load_dotenv


def get_breeds(base_url: str, headers: dict, *, limit: int = 10, page: int = 0) -> str:
    params = {"limit": limit, "page": page}

    res = requests.get(f"{base_url}breeds", headers=headers, params=params, timeout=1)

    res.raise_for_status()

    if res.ok:
        return res.json()


def image_search(base_url: str, headers: dict, *, limit: int = 10, page: int = 0) -> str:
    params = {"limit": limit, "page": page, "size": "small", "order": "ACS", "has_breeds": True, "mime_types": "jpg"}
    res = requests.get(f"{base_url}images/search", headers=headers, params=params, timeout=5)

    return res.json()


def main():
    load_dotenv()
    base_url = "https://api.thedogapi.com/v1/"
    headers = {"Content-Type": "application/json", "x-api-key": os.getenv("API_KEY")}

    # get the first 10 breeds from the API
    # breeds = get_breeds(base_url, headers)
    # pprint.pprint(breeds, indent=2)

    # get all the breed from API
    # page = 0
    # with open("breed-list.txt", mode="w", encoding="utf-8") as f:
    #     while True:
    #         breeds = get_breeds(base_url, headers, page=page)
    #         if not breeds:
    #             break
    #         # pprint.pprint(breeds, indent=2)
    #         for breed in breeds:
    #             f.write(f"{breed['name']}\n")

    #         page += 1

    images = image_search(base_url, headers)
    for image in images:
        print(f'{image["breeds"][0]["name"]}:')
        image_url = image["url"]
        filename = image["id"] + ".jpg"
        image = requests.get(image_url, timeout=1, stream=False)
        image.raw.decode_content = True
        with open(filename, "wb") as outfile:
            outfile.write(image.content)
        output = climage.convert(filename, is_256color=False, is_truecolor=True, is_unicode=True, width=120)
        print(output)

    # pprint.pprint(images)
    return 0


if __name__ == "__main__":
    sys.exit(main())
