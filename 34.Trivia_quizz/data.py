import requests

url = "https://opentdb.com/api.php?amount=30&category=18&type=boolean"
data = requests.get(url=url)
data.raise_for_status()
question_data = data.json()
question_data = question_data["results"]