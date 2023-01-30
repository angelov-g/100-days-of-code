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
# Method 1
# drop: bool, default True
# Delete columns to be used as the new index
# inplace: bool, default False
# Whether to modify the DataFrame rather than creating a new one
birthdays_df.set_index(["month", "day"], drop=False, inplace=True)
birthdays_dict = birthdays_df.to_dict("index")

# Method 2 - Dictionary Comprehension
# birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays_df.iterrows()}

if today_date in birthdays_dict:
    birthday_person = birthdays_dict[today_date]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_template:
        original_letter = letter_template.read()

    birthday_message = original_letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n"
                                f"{birthday_message}"
                            )
