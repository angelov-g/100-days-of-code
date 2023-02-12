import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "ajshd18u43j3rowad",
    "username": "angelov-g",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
