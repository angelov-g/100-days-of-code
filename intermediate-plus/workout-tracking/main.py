import requests
from datetime import datetime

APP_ID = "APP ID"
APP_KEY = "APP KEY"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
today = datetime.now().strftime("%d/%m/%Y")
time = (datetime.now().strftime("%H:%M:%S"))

performed_exercises = input("Tell me what exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_config = {
    "query": performed_exercises,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 182,
    "age": 24
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
response_data = response.json()

sheety_endpoint = "https://api.sheety.co/4ff6909e4841189431a21ec2b500b261/workoutTracking/workouts"

for exercise in response_data["exercises"]:
    sheety_config = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_config)
