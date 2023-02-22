import requests
import lxml
from bs4 import BeautifulSoup

TARGET_PRICE = 90

HEADERS = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/109.0.0.0 Safari/537.36"
}

URL = "https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=sr_1_1_sspa?crid=29A0YQ3Z4STW7" \
      "&keywords=rice+cooker&qid=1677076450&sprefix=rice+coo%2Caps%2C206&sr=8-1-spons&psc=1" \
      "&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMTdERFVFQ01DUU41JmVuY3J5cHRlZEl" \
      "kPUEwMjAzNzYxMTA0WjI3TENZUEhOQSZlbmNyeXB0ZWRBZElkPUEwNzU5NzMxNkJa" \
      "UDdZV0ROMEoxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

response = requests.get(URL, headers=HEADERS)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")

price = soup.find(name="span", class_="a-offscreen").getText()
price_number = float(price.split("$")[1])

# In the original challenge this was supposed to be sent with an email using the SMTP module.
if price_number < TARGET_PRICE:
    print(f"Your item now costs {price}! You should consider buying.")
