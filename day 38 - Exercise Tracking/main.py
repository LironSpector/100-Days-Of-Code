import requests
from datetime import datetime
import os


# APP_ID = "d90a497b"
# API_KEY = "3082f07c629e40c6a12bc373498912e3"
# TOKEN = "f7f8hky85kdmij65do"
# SHEET_ENDPOINT = "https://api.sheety.co/6104db415a803f72d8302362981649d9/workoutTracking/workouts"
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

GENDER = "male"
WEIGHT_KG = 52
HEIGHT_CM = 165
AGE = 15

TOKEN = os.environ.get("TOKEN")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content": "json"
}

params_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=params_data, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%Y/%m/%d")
today_time = datetime.now().strftime("%X")

bearer_headers = {"Authorization": f"Bearer {TOKEN}"}

for exercise in result["exercises"]:
    workout = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=workout, headers=bearer_headers)
    print(response.text)
