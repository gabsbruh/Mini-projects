import requests
import datetime as dt
import json
import os

### ENVIRONMENTAL VARIABLES
sheet_auth_headers = {"Authorization": os.environ.get('SHEETY_BEARER_TOKEN')}
sheety_url = os.environ.get('SHEETY_URL')
auth_header = {
    "x-app-id": os.environ.get('NUTRITIONIX_APP_ID'),
    "x-app-key": os.environ.get('NUTRITIONIX_API_KEY'),
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


### NUTRITIONIX - query for get info about workout ###
# query
query = str(input("What exercises you did today?: "))
query_params = {
    "query": query,
}

# post
response = requests.post(url=exercise_endpoint, json=query_params, headers=auth_header)
result = response.json()
exercise = result['exercises'][0]['name']
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']


### SHEETY - log data to spreadsheet ###
# date
today = dt.datetime.today()
hour = today.hour if today.hour >= 10 else f"0{today.hour}"
minute = today.minute if today.minute >= 10 else f"0{today.minute}"

# params to add to the row in the spreadsheet
add_row_params ={
    "workout": {
        "date": str(today.date()),
        "time": f"{hour}:{minute}",
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

response2 = requests.post(url=sheety_url, json=add_row_params, headers=sheet_auth_headers)
print(response2.text)
