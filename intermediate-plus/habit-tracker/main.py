import requests

TOKEN = "ajshd18u43j3rowad"
USERNAME = "angelov-g"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# CREATE USER
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# CREATE GRAPH available at https://pixe.la/v1/users/angelov-g/graphs/graph1
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

add_pixel_config = {
    "date": "20230212",
    "quantity": "10"
}

response = requests.post(url=add_pixel_endpoint, json=add_pixel_config, headers=headers)
print(response.text)
