import requests
from datetime import datetime
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "R45GTVW6RL5AS4CU"
NEWS_API_KEY = "5345386fdbe64912ba3490e90b42e75b"

TWILIO_ACCOUNT_SID = "AC013492e5e6952c249d41eccb84e9a248"
TWILIO_AUTH_TOKEN = "b949a8c45c28f908360a1da1fc5044cf"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

data_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_URL, params=data_parameters)
response.raise_for_status()
data = response.json()

now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
if now.month < 10:
    current_month = f"0{current_month}"

yesterday = f"{current_year}-{current_month}-{current_day - 1}"
day_before_yesterday = f"{current_year}-{current_month}-{current_day - 2}"

yesterday_closing_price = float(data["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_closing_price = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])

different_in_percentage = 100 - round(yesterday_closing_price / day_before_yesterday_closing_price * 100)
up_down = None
if yesterday_closing_price > day_before_yesterday_closing_price:
    different_in_percentage = abs(different_in_percentage)
    up_down = "⬆"
else:
    up_down = "⬇"

if abs(different_in_percentage) >= 5:
    news_parameters = {
        "q": COMPANY_NAME,
        "from": f"{current_year}-{current_month}-{current_day}",
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url=NEWS_API_URL, params=news_parameters)
    response.raise_for_status()

    news_api_data = response.json()
    articles = news_api_data["articles"]
    three_articles = articles[:3]

    formatted_articles = [f'{STOCK}: {up_down}{different_in_percentage}%\n' \
                          f'Headline: {article["title"]}.\nBrief: {article["description"]}'
                          for article in three_articles]

    for article in formatted_articles:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                body=article,
                from_="+19893651823",
                to="+972 53 965 4065"
            )
