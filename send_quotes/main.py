import smtplib
from datetime import date, datetime
import random 
import os
from dotenv import load_dotenv

load_dotenv()

with open("send_quotes/quotes.txt") as file:
    contents = file.readlines()

day_of_week = datetime.weekday(datetime.now())

def get_random_quote():
    return random.choice(contents)

def send_email():
    my_email = os.getenv('MY_EMAIL')
    password = os.getenv('PASSWORD')
    to_email = os.getenv('TO_EMAIL')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Motivational Quote\n\n{get_random_quote()}")

if day_of_week == 3:
    send_email()

