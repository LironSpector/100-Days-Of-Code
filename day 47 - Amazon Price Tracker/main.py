import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "lirontheprog@gmail.com"
MY_PASSWORD = "ciexaniegletpvnu"

headers = {
    "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

sheety_url = "https://api.sheety.co/6104db415a803f72d8302362981649d9/amazonProducts/products"

authorization = {
    "Authorization": "Bearer cdnjgnrkjgnbvgfkjsrg"
}

response = requests.get(url=sheety_url, headers=authorization)
products = response.json()["products"]

for product in products:
    url = product["url"]
    acceptable_price = product["lowestPrice"]
    product_name = product["productName"]

    response = requests.get(url=url, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, "lxml")

    price = soup.find(name="span", dir="ltr").get_text()
    price_without_currency = price.split("$")[1].replace("\u200e", "")
    price_as_float = float(price_without_currency)

    if price_as_float < float(acceptable_price):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Instant Pot Price Alert!\n\n{product_name} price is now ${price_as_float},"
                    f" below your target price. Buy now!")
