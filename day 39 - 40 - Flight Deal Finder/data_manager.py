import requests
import json

PRICES_SHEETY_ENDPOINT = "https://api.sheety.co/6104db415a803f72d8302362981649d9/flightDeals/prices"
USERS_SHEETY_ENDPOINT = "https://api.sheety.co/6104db415a803f72d8302362981649d9/flightDeals/users"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_price_data = {}
        self.destination_users_data = {}

    def get_data(self):
        response = requests.get(url=PRICES_SHEETY_ENDPOINT)
        self.destination_price_data = json.loads(response.text)["prices"]
        return self.destination_price_data

    def update_sheet_data(self):
        for city in self.destination_price_data:
            put_params = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{PRICES_SHEETY_ENDPOINT}/{city['id']}", json=put_params)
            # print(response.text)

    def get_users_data(self):
        response = requests.get(url=USERS_SHEETY_ENDPOINT)
        self.destination_users_data = json.loads(response.text)["users"]
        return self.destination_users_data
