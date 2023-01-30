import smtplib

my_email = "angelov.abw@gmail.com"
my_password = "dzpbztilkolmxqkw"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg="Subject:Hello\n\n"
                            "This is the body of the email."
                        )
