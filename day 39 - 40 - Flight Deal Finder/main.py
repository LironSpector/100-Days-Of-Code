from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

sheet_data = data_manager.get_data()
# print(sheet_data)

is_clear = True
for dic in sheet_data:
    if dic["iataCode"] != "":
        is_clear = False

if is_clear:
    for dic in sheet_data:
        dic["iataCode"] = flight_search.get_destination_code(dic["city"])

    data_manager.destination_price_data = sheet_data
    data_manager.update_sheet_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight_data = flight_search.search_flights(origin_city_code=ORIGIN_CITY_IATA,
                                               destination_city_code=destination["iataCode"],
                                               date_from=tomorrow,
                                               date_to=six_month_from_today)

    if flight_data.price < destination["lowestPrice"]:
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight_data.origin_airport}.{flight_data.destination_airport}" \
               f".{flight_data.out_date}*{flight_data.destination_airport}.{flight_data.origin_airport}.{flight_data.return_date}"

        message = f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport}" \
                  f" to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}." \
                  f"\n{link}"

        users_sheet_data = data_manager.get_users_data()
        for user in users_sheet_data:
            email = user["email"]
            notification_manager.send_email(message.encode("utf-8"), email)
