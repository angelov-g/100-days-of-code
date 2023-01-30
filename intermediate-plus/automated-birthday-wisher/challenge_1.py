import smtplib
import datetime as dt
import random

MY_EMAIL = "asjkleh982y1ehdijka@outlook.com"
MY_PASSWORD = "Parola1234@"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:  # Monday
    with open("quotes.txt") as quotes:
        list_quotes = quotes.readlines()
    daily_quote = random.choice(list_quotes)

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Daily Motivational Quote\n\n"
                                f"{daily_quote}"
                            )
