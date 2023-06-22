import requests
from datetime import datetime


USERNAME = "lirontheprog"
TOKEN = "fj448gdjk4itnf43hu"
GRAPH_ID = "graph1"
TODAY = datetime.now().strftime("%Y%m%d")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_CREATION_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
PIXEL_UPDATE_ENDPOINT = f"{PIXEL_CREATION_ENDPOINT}/{TODAY}"
PIXEL_DELETE_ENDPOINT = PIXEL_UPDATE_ENDPOINT

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_config = {
    "id": GRAPH_ID,
    "name": "Book_Tracker_Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)

pixel_data = {
    "date": TODAY,
    "quantity": input("How many pages did you read today?")
}

response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)

update_pixel_data = {
    "quantity": "15"
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=update_pixel_data, headers=headers)
# print(response.text)

# response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
