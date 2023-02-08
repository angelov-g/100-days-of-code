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
weather_slice = weather_data["list"][:6]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    