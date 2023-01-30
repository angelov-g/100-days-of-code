# import smtplib
#
# my_email = "angelov.abw@gmail.com"
# my_password = "dzpbztilkolmxqkw"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=my_email,
#                         msg="Subject:Hello\n\n"
#                             "This is the body of the email."
#                         )

import datetime as dt

now = dt.datetime.now()
year = now.year
dow = now.weekday()
print(dow)

date_of_birth = dt.datetime(year=2005, month=1, day=30, hour=4, minute=20)
print(date_of_birth)