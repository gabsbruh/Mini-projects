import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 49.706070 # Your latitude
MY_LONG = 20.420790 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
while True:
    if  (MY_LAT - 5 < iss_latitude < MY_LAT + 5) and (MY_LONG - 5 < iss_latitude < MY_LONG + 5): #Your position is within +5 or -5 degrees of the ISS position.
        if sunset < time_now.hour or sunrise > time_now.hour:
            # Then send me an email to tell me to look up.
            with smtplib.SMTP(host="smtp.gmail.com") as connect:
                my_email = "XXXXXXXXXXX@gmail.com"
                connect.starttls()
                connect.login(user=my_email, password="XXXXXXXXXXXXXXXX")
                connect.sendmail(from_addr=my_email, to_addrs=my_email, 
                                message="Subject:Look Up!\n\n ISS is above you!")
    time.sleep(60)
