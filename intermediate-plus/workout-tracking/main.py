import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = "APP ID"
APP_KEY = "APP KEY"

# Endpoints
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/4ff6909e4841189431a21ec2b500b261/workoutTracking/workouts"

# Request to Nutritionix
performed_exercises = input("Tell me what exercises you did: ")
exercise_config = {
    "query": performed_exercises,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 182,
    "age": 24
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
response_data = response.json()

# Request to the sheety
today_date = datetime.now().strftime("%d/%m/%Y")
time_now = (datetime.now().strftime("%H:%M:%S"))

# Basic authentication
basic = HTTPBasicAuth("angelov-g", "PASSWORD")

for exercise in response_data["exercises"]:
    sheety_config = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_config, auth=basic)
