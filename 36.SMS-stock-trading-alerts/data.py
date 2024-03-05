import requests
import json
from main import RANGE_OF_DAYS, STOCK_COMPANY_NAME

# grab stock prices data from alphaadvantage API. last 100 records every 30 min starting from most recent
api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
company_name = "Tesla Inc"
url = 'https://www.alphavantage.co/query'
params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_COMPANY_NAME,
    "interval": "30min",
    "apikey": api_key,
    "outputsize": "compact",
}
r = requests.get(url=url, params=params)
data = r.json()

with open("data.json", "w") as datafile:
    json_object = json.dumps(data, indent=4)
    datafile.write(json_object)
    
# grab stock news data from API
api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
url = 'https://newsapi.org/v2/everything'
params = {
    "q": company_name,
    "from": RANGE_OF_DAYS[1],
    "to": RANGE_OF_DAYS[0],
    "sortBy": "popularity",
    "apikey": api_key,
    "language": "en",
    "pageSize": 5
}
r = requests.get(url=url, params=params)
data = r.json()

with open("news.json", "w") as datafile:
    json_object = json.dumps(data, indent=4)
    datafile.write(json_object)