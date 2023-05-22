#!/usr/bin/env python3
import os

import dotenv  # pip install python_dotenv
import requests

dotenv.load_dotenv()  # load all the variables in .env file into the system environment

api_key = os.getenv("ACCU_WEATHER_API_KEY")  # load the value
user_name = os.getenv("USER_NAME")  # load the value
password = os.getenv("PASSWORD")  # load the value

print(api_key)
