# Code doesn't work with OneCall due to API being subscription based now

import os
import requests
from twilio.rest import Client

api_key = "TWILIO_API_KEY"
account_sid = "TWILIO_SID"
auth_token = "TWILIO_AUTH_TOKEN"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 43.214050,
    "lon": 27.914734,
    "appid": api_key
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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+17575178480",
        to="+XXXXXXXXX"
    )

    print(message.status)