import pandas as pd
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
date = (now.day, now.month) # sign today's date into a tuple

# read csv with pandas
birthdays = pd.read_csv('birthdays.csv')
today_birthdays = {}# store today's birthdays in namedtuple (let's try this type)
for _,row in birthdays.iterrows():
    if row['day'] == date[0] and row['month'] == date[1]:
        today_birthdays[row['name']] = row['email']

# replace name in the letter for each user
letter_lists = {} # {email:letter}
for (name, email) in today_birthdays.items():
    # take random letter between 1 and 3
    with open(f'letter_templates\letter_{random.randint(1,3)}.txt') as letter:
        letter_content = letter.read()
    personalized = letter_content.replace("[NAME]", name) # personalize letter by
    # changing [NAME] to a specific name from today_birthdays list
    letter_lists[email] = personalized

# create connection
with smtplib.SMTP(host="smtp.gmail.com", port=587) as connect:
    connect.starttls() # secure the connection
    # log in to the account. I've hidden my personal data
    my_email = "XXXXXXXXXXX@gmail.com"
    connect.login(user=my_email, password="XXXXXXXXXXXXXXXX") 
    for (email, letter) in letter_lists.items(): # send email for each person with today's birthdays
        connect.sendmail(from_addr=my_email, to_addrs=email,
                         msg=f"Subject:Birthday Wishes :)\n\n{letter}")
