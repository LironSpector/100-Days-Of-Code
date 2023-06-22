import requests

USERS_SHEETY_ENDPOINT = "https://api.sheety.co/6104db415a803f72d8302362981649d9/flightDeals/users"

print("Welcome to Liron's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
repeat_email = input("Type your email again:\n")

if email == repeat_email:
    user_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    response = requests.post(url=USERS_SHEETY_ENDPOINT, json=user_data)
    response.raise_for_status()
    data = response.json()
    print(data)
    print("Welcome to the club!")
