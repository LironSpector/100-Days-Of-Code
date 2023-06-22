import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PRICE_API_KEY = "R45GTVW6RL5AS4CU"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "5345386fdbe64912ba3490e90b42e75b"

TWILIO_ACCOUNT_SID = "AC013492e5e6952c249d41eccb84e9a248"
TWILIO_AUTH_TOKEN = "b949a8c45c28f908360a1da1fc5044cf"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_PRICE_API_KEY
}

# response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
# response.raise_for_status()
# data = response.json()
# print(data)

response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=R45GTVW6RL5AS4CU")
response.raise_for_status()
data = response.json()

list_of_dicts = [value for (key, value) in data["Time Series (Daily)"].items()]
yesterday = list_of_dicts[0]
yesterday_price = float(yesterday["4. close"])
day_before_yesterday = list_of_dicts[1]
day_before_yesterday_price = float(day_before_yesterday["4. close"])

difference = abs(yesterday_price - day_before_yesterday_price)
diff_percent = difference / yesterday_price * 100
if diff_percent >= 5:
    if yesterday_price > day_before_yesterday_price:
        symbol = f"+ {round(diff_percent)}"
    else:
        symbol = f"- {round(diff_percent)}"

    news_params = {
        "apikey": NEWS_API_KEY,
        "sort_by": "relevancy",
        "qInTitle": COMPANY_NAME
    }

    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    articles = response.json()["articles"]

    for i in range(2):
        article = articles[i]
        title = article["title"]
        description = article["description"]
        message_text = f"{STOCK}: {symbol}%\nHeadLine: {title}.\nBrief: {description}"

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages \
            .create(
            body=message_text,
            from_='+15617833092',
            to='+972 53 965 4065'
            )
