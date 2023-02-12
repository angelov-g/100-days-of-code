import requests
from datetime import datetime

TOKEN = "ajshd18u43j3rowad"
USERNAME = "angelov-g"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

# CREATE USER
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# CREATE GRAPH available at https://pixe.la/v1/users/angelov-g/graphs/graph1.html
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Format today's date to match the API date format
today = datetime.now().strftime("%Y%m%d")

# ADD PIXEL TO GRAPH
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

add_pixel_config = {
    "date": today,
    "quantity": "10"
}

# response = requests.post(url=add_pixel_endpoint, json=add_pixel_config, headers=headers)
# print(response.text)

# UPDATE PIXEL
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_pixel_config = {
    "quantity": "15"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# DELETE PIXEL
# endpoint is the same as the update pixel endpoint
# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)
