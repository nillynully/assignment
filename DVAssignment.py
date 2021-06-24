#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import requests
import yfinance as yf


# In[5]:


import cufflinks as cf 


# In[6]:


init_notebook_mode(connected=True)
cf.go_offline()


# In[7]:


aapl= yf.Ticker("aapl")
aapl


# In[10]:


aapl_historical = aapl.history(period="max", interval="1wk")
aapl_historical


# In[11]:


aapl_historical.iplot


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


# RSI Formula
def RSI(ohlc, period = 14, method = "SMA"):
    delta = ohlc["Close"].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    
    if method == "SMA":
        gain - up.rolling(period).mean()
        loss = down.abs().rolling(period).mean()
    else:
        gain = up.ewm(span = period).mean()
        loss = down.abs().ewm(span = period).mean()
        
    RS = gain/loss
    ohlc["RSI"] = pd.Series(100 - (100/(1+RS)), name ="RSI")
    
    return ohlc


# In[ ]:


tickers = ["FB", "AAPL", "AMZN", "IBM", "GOOGL", "MSFT", "NAV", "O", "QCOM", "TSLA"]
ticker_list = []
stock_num = 1
while True:
    try:
        num_stock = int(input("Enter number of stocks between 1 - 10: "))
    except ValueError:
        print("Sorry, please only key in numbers")
    else:
        break

for i in tickers:
    print(f"Choose stock number {stock_num} from following stocks. \n {([i for i in tickers if i not in ticker_list])}")
    print()
    in_2 = input("Enter your stock: ")
    print()
    ticker_list.append(in_2)
    
    if stock_num == int(num_stock):
        choice_1 = input("Please indicate whether you would like to use the EWMA or SMA to compute the RSI Value: ")
        choice_2 = input("Please enter the Moving Window range: ")
        choice_3 = input("Please enter start date for the chart between 2010-01-01 and 2017-12-31, in YYYY-MM-DD format here: ")
        choice_4 = input("Please enter end date for the chart between 2010-01-01 and 2017-12-31, in YYYY-MM-DD format here: ")
        dt = datetime.strptime(choice_3,"%Y-%m-%d")
        start_date = int(round(dt.timestamp()))
        dt1 = datetime.strptime(choice_4,"%Y-%m-%d")
        end_date = int(round(dt1.timestamp()))
        
        for i in ticker_list:
            df = yf.download({ticker_list}, start = start_date, end = end_date)
            
        
    
        

        
       


# In[ ]:


new_columns = ["Tickers", "RSI"] 
final_dataframe = pd.DataFrame(columns = new_columns)
final_dataframe


# In[ ]:


tickers = ["FB", "AAPL", "AMZN", "IBM", "GOOGL", "MSFT", "NAV", "O", "QCOM", "TSLA"]

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

querystring = {"symbol":"FB"}

headers = {
    'x-rapidapi-key': "3ce5bf2bf3mshfaf1906b19b78c4p1e60e7jsn33601bc0e1b9",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# 
