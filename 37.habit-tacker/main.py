import requests
import datetime as dt

USERNAME = "XXXXXXX"
TOKEN = "XXXXXXXXXX"
pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN
}


## CREATE ACCOUNT ###
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


### CREATE GRAPH ###
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
print(graph_endpoint)
graph_params = {
    "id": 'graph1',
    'name':'cycling graph',
    'unit': 'km',
    'type': 'float',
    'color': 'sora',
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

print(response.text)


### POST PIXEL ###
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
# date
date = dt.datetime.today().date()
date -= dt.timedelta(days=2)
date = str(date)
date = date.replace("-", "")

post_params = {
    'date': date,
    'quantity': "20",
}
response = requests.post(url=post_endpoint, json=post_params, headers=headers)
print(response.text)


### PUT PIXEL ###
date
date = dt.datetime.today().date()
date -= dt.timedelta(days=1)
date = str(date)
date = date.replace("-", "")

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"

put_params = {
    'quantity': "15",
}
response = requests.put(url=put_endpoint, json=put_params, headers=headers)
print(response.text)


### DELETE PIXEL ###
date = dt.datetime.today().date()
date -= dt.timedelta(days=7)
date = str(date)
date = date.replace("-", "")

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"

put_params = {
    'quantity': "15",
}
response = requests.delete(url=put_endpoint, headers=headers)
print(response.text)
