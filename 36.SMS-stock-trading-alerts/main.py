import datetime as dt
import json
from twilio.rest import Client


today = dt.datetime.today().date()
delta = dt.timedelta(days=1) # equals to 1 day, subtractable from today's date
# CONSTANTS
DAYS_BACK = 5
RANGE_OF_DAYS = (today-delta, today-DAYS_BACK*delta) # parameter for news api to which days to look for the news
DEGREE_OF_SENSIVITY = 0.01+5 # how much reative change should be in stock price to be notified with infos?
STOCK_COMPANY_NAME = "TSLA" # for data extraction from api
NUMBER_OF_NEWS = 3 # how much news user will get in SMS


## TODO 1:
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# import data
with open('data.json', 'r') as datafile:
    json_data = datafile.read()
data = json.loads(json_data) # convert json data to dict

try:
    def max_stock_price(data: dict, date: dt.datetime, days_back_min: int=0, days_back_max: int=0) -> float:
        """return max value of 'close' variable from data on specified day

        Args:
            data (dict): data with registered stock prices
            date (dt.datetime): date to look for in the data
            days_back_min (int): minimum difference of time to look for data
            days_back_max (int): maximum difference of time to look for data. 
            default variables is set to look for only today.

        Returns:
            (float): max value in specified data
        """
        stock_prices = []
        for day in range(days_back_min, days_back_max+1):
            for (key, value) in data["Time Series (30min)"].items():
                if (str(date - delta*day)) in key:
                    stock_prices.append(value["4. close"]) 
            if len(stock_prices) > 0:
                return max(stock_prices)
    yesterday_max_stock_price = float(max_stock_price(data, today, days_back_min=1, days_back_max=1))
    two_day_ago_max_stock_price = float(max_stock_price(data, today, days_back_min=2, days_back_max=DAYS_BACK)) #2-days back
    
except (KeyError):
    raise Exception("RateLimitExceededError:\tAPI rate limit is 25 requests per day")

except (TypeError):
    raise Exception(f"The data is outdated ({today}). Run the data file to fetch the latest data.")


## TODO 2:
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# when stock price changed more than 5% recently, get news 

relative_change = (yesterday_max_stock_price - two_day_ago_max_stock_price)/max([yesterday_max_stock_price, two_day_ago_max_stock_price])
if relative_change >= DEGREE_OF_SENSIVITY or relative_change <= -DEGREE_OF_SENSIVITY:
    # import news data
    with open('news.json', 'r') as datafile:
        json_data = datafile.read()
    news = json.loads(json_data) # convert json data to dict
    is_stock_price_up = "🔺" if relative_change > 0 else "🔻"
    #form message to SMS
    message = [f"{STOCK_COMPANY_NAME}: {is_stock_price_up} {round(abs(relative_change)*100, 2)}%"]
    for number in range(NUMBER_OF_NEWS):
        url = news["articles"][number]["url"]
        title = news["articles"][number]["title"]
        content = news["articles"][number]["description"]
        message.append(f"Headline: {title}\nBrief: {content}\nURL:{url}")
    message = "\n\n".join(message)


## TODO 3:
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
if relative_change >= DEGREE_OF_SENSIVITY or relative_change <= -DEGREE_OF_SENSIVITY:
    account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+12XXXXXXXXX',
    body=message,
    to='+48XXXXXXXXX'
    )
