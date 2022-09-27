# API Autentificação Avançada e POST/PUT/DELETE request
from datetime import datetime

import requests

UNM = "piresrenan"
TKN = "a56gfdASDF5asdfASDF5411"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TKN,
    "username": UNM,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{UNM}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    'X-USER-TOKEN': TKN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{UNM}/graphs/{GRAPH_ID}"

today = datetime(year=2022, month=7, day=29)
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{UNM}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{UNM}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
