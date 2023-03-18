import requests
from dotenv import load_dotenv
import os
import json
import datetime

today = datetime.datetime.now()

year = today.year
month = today.month
day = today.day

# print(day, month, year)

load_dotenv(".env")

# print(os.getenv('NEWS_API_KEY'), os.getenv('PATH'))

STOCK = "TSLA"
COMPANY_NAME = "meta"

NEWS_URL = "https://newsapi.org/v2/top-headlines"
news_params = {
    "apiKey": os.getenv('NEWS_API_KEY'),
    "q": COMPANY_NAME, 
}

news_response = requests.get(url=NEWS_URL, params=news_params)
news_response.raise_for_status()
print(news_response.status_code)
news_data = news_response.json()
# print(news_data)
with open('D:/documents/Python lessons/AngelaYu/day36-trading/news.txt', 'w') as news_file:
    news_file.write(json.dumps(news_data))


STOCK_DATA_URL = "https://www.alphavantage.co/query"
stock_data_params = {
    "apikey": os.getenv("STOCK_API_KEY"),
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min"
}

stock_response = requests.get(url=STOCK_DATA_URL, params=stock_data_params)
stock_response.raise_for_status()
print(stock_response.status_code)
stock_data = stock_response.json()
# print(type(stock_response), type(stock_data))
# print(stock_data)
with open('D:/documents/Python lessons/AngelaYu/day36-trading/stock.txt', 'w') as stock_file:
    stock_file.write(json.dumps(stock_data))
# print(type(json.dumps(stock_data)))

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


narrow = stock_data['Time Series (Daily)']

value_list = [values for key, values in narrow.items()]
key_list = [key for key, values in narrow.items()]
# print(key_list, '\n*********\n', value_list)

today_close = float(value_list[0]['4. close'])
yest_close = float(value_list[1]['4. close'])

# print(today_close, '\n', yest_close)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

article_list = news_data["articles"]

a, b, c = article_list[:3]

print(a, '\n*****', b, '\n*****', c)
print(os.getenv("STOCK_API_KEY"))
print(os.getenv('NEWS_API_KEY'))
    

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""



