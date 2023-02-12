import requests

APP_ID = "APP ID"
APP_KEY = "APP KEY"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key": APP_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

performed_exercises = input("Tell me what exercises you did: ")

exercise_config = {
    "query": performed_exercises,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 182,
    "age": 24
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
print(response.text)
