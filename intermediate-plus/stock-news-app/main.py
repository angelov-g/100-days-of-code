import requests
import datetime

up_down = None
today = datetime.date.today()
delta = datetime.timedelta(days=1)
yesterday = today - delta
before_yesterday = yesterday - delta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "7C86ZIAJ6MWUOU8T"
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "bb989c705e85477bb64032e12cd404d0"
news_params = {
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday_data = stock_data["Time Series (Daily)"][str(yesterday)]
yesterday_closing_price = float(yesterday_data["4. close"])

before_yesterday_data = stock_data["Time Series (Daily)"][str(before_yesterday)]
before_yesterday_closing_price = float(before_yesterday_data["4. close"])
difference = yesterday_closing_price - before_yesterday_closing_price

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / yesterday_closing_price) * 100)

if abs(diff_percent) > 1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_articles = news_data["articles"][:3]
    formatted_articles = [f"{STOCK}{up_down}{diff_percent}%."
                          f"\nHeadline: {article['title']}."
                          f"\nBrief: {article['description']}" for article in news_articles]
    for article in formatted_articles:
        print(article)


