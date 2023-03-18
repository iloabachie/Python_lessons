import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf

webpage_df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
len(webpage_df)
# print(type(webpage_df[0]))
webpage_df = webpage_df[0]
# print(webpage_df.head(15))

# print(webpage_df.describe(include='all'))
# print(webpage_df.info())

# print(webpage_df.Symbol.unique())

# print(webpage_df['GICS Sector'].unique())

# print(webpage_df[webpage_df['GICS Sector'] == 'Energy'])

energy_data = webpage_df[webpage_df['GICS Sector'] == 'Energy']

stock_list = energy_data.Symbol.unique()

start_date = dt.datetime(2021,9,29)
end_date = dt.datetime.today()

stock_price = pd.DataFrame() # create empty dataframe

tsla_stock = yf.download('TSLA', start_date, end_date)
# print(tsla_stock)

tsla_stock.to_csv('tesla')
# for ticker in stock_list:
#     price = yf.download(ticker, start_date, end_date)
#     price['Symbol'] = ticker
#     stock_price.append(price) # does not work.
#     stock = pd.concat(price)
#     print(price.head(10))
#     print(stock.head(6))

print(stock_price)

import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(x = tsla_stock.index, 
    open = tsla_stock['Open'],
    high = tsla_stock['High'],
    low = tsla_stock['Low'],
    close = tsla_stock['Close'])])

# print(fig)
print(type(fig))
# fig.show()
print(dir(go.Figure))


tsla_stock = tsla_stock.reset_index(inplace=True)
tsla_stock