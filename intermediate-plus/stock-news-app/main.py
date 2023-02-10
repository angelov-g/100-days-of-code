import requests
import datetime

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
    "q": COMPANY_NAME,
    "apikey": NEWS_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday_data = stock_data["Time Series (Daily)"][str(yesterday)]
yesterday_closing_price = float(yesterday_data["4. close"])

before_yesterday_data = stock_data["Time Series (Daily)"][str(before_yesterday)]
before_yesterday_closing_price = float(before_yesterday_data["4. close"])
difference = abs(yesterday_closing_price - before_yesterday_closing_price)
diff_percent = (difference / yesterday_closing_price) * 100

if diff_percent > 5:
    print("Get News")

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

