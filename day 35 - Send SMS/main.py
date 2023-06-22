import requests
from twilio.rest import Client

MY_LAT = 31.046051
MY_LONG = 34.851612

own_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "278c619b45a8195c43dfc1f59b66bff4"
account_sid = "AC013492e5e6952c249d41eccb84e9a248"
auth_token = "b949a8c45c28f908360a1da1fc5044cf"

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url=own_endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

need_umbrella = False

for hour in range(12):
    if weather_data["hourly"][hour]["weather"][0]["id"] < 700:
        need_umbrella = True

if need_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella ☂️",
            from_="+19893651823",
            to="+972 53 965 4065"
        )

    print(message.status)
