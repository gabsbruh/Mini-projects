import requests
import json
from twilio.rest import Client

# Data inside the code which is personal was replaced with XXX

# input paramters to api call
# limanowa, pl
my_weather_params = {
    "lat": "49.706070",
    "lon": "20.420790",
    "appid": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "cnt": 4
}

api_call = "https://api.openweathermap.org/data/2.5/forecast"

# get request
data = requests.get(url=api_call, params=my_weather_params)
data.raise_for_status()
json_data = data.json()

# save data to the file
with open("test1.json", "w") as json_file:
    json_object = json.dumps(json_data, indent=4)
    json_file.write(json_object)

# create list contains booleans informs wheter it rains in next 12 hours or not
is_weather_condition_below_700 = [entry["weather"][0]["id"] < 700 for entry in json_data["list"]]

# Twilio login
account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    
# if any item is true in this list, print feedback to bring an umbrella
if any(is_weather_condition_below_700):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+12XXXXXXXXX',
    body="It's going to rain today. Remember to bring an umbrella!!",
    to='+48XXXXXXXXX'
    )