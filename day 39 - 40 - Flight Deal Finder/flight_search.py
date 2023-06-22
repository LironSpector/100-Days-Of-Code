import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API = "HCwynAQRBVu8WsdC4nkSXjZEooEDAvMI"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        headers = {
            "apikey": TEQUILA_API,
        }

        tequila_params = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=tequila_params, headers=headers)
        response.raise_for_status()
        results = response.json()["locations"]

        code = results[0]["code"]
        return code

    def search_flights(self, origin_city_code, destination_city_code, date_from, date_to):
        headers = {
            "apikey": TEQUILA_API,
        }

        search_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=search_params, headers=headers)
        response.raise_for_status()
        data = response.json()["data"][0]

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        # print(f"{flight_data.destination_city}: £{flight_data.price}, {flight_data.origin_city}")

        return flight_data
