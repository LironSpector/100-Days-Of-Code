import requests

url = input("Please enter a URL: ")
acceptable_price = input("What is the highest price you agree to pay on the product? ")
product_name = input("What is the product name? ")

sheety_url = "https://api.sheety.co/6104db415a803f72d8302362981649d9/amazonProducts/products"

authorization = {
    "Authorization": "Bearer cdnjgnrkjgnbvgfkjsrg"
}

params = {
    "product": {
        "url": url,
        "lowestPrice": acceptable_price,
        "productName": product_name
    }
}

response = requests.post(url=sheety_url, json=params, headers=authorization)
print(response.text)
