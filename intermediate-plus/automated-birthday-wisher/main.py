import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "asjkleh982y1ehdijka@outlook.com"
MY_PASSWORD = "Parola1234@"

today_day = dt.datetime.now().day
today_month = dt.datetime.now().month
today_date = (today_month, today_day)

birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_df.set_index(["month", "day"], drop=True, inplace=True)
birthdays_dict = birthdays_df.to_dict("index")

if today_date in birthdays_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_template:
        original_letter = letter_template.read()

    birthday_message = original_letter.replace("[NAME]", birthdays_dict[today_date]["name"])

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthdays_dict[today_date]["email"],
                            msg=f"Subject:Happy Birthday\n\n"
                                f"{birthday_message}"
                            )
