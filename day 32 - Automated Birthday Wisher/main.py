import smtplib
import datetime as dt
import pandas
import random


MY_EMAIL = "lirontheprog@gmail.com"
MY_PASSWORD = "programmer#1"

birthdays_data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()

for (index, row) in birthdays_data.iterrows():
    if row.month == now.month and row.day == now.day:
        name = birthdays_data.name[index]
        email = birthdays_data.email[index]
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as text_file:
            content = text_file.read()
            greeting = content.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{greeting}")
