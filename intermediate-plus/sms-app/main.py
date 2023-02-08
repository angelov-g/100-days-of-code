# Code doesn't work with OneCall due to API being subscription based now

import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 43.214050,
    "lon": 27.914734,
    "appid": "10d2b45dd5ae375803d151072d5af8ae"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])
