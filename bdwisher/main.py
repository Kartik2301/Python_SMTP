##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import random
import smtplib
from datetime import datetime
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

now = datetime.now()
cur_day = now.day
cur_month = now.month

def get_wish(name):
    files = os.listdir("bdwisher/letter_templates/")
    random_file = random.choice(files)
    with open(f"bdwisher/letter_templates/{random_file}") as file:
        content = file.read()
        content = content.replace("[NAME]", name)
    return content

def send_email(name):
    my_email = os.getenv('MY_EMAIL')
    password = os.getenv('PASSWORD')
    to_email = os.getenv('TO_EMAIL')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Happy Birthday {name}\n\n{get_wish(name)}"
        )
    print("Email Sent")

birthday_list = pd.read_csv("bdwisher/birthdays.csv")
for (index, row) in birthday_list.iterrows():
    if row["month"] == cur_month and row["day"] == cur_day:
        send_email(row["name"])
