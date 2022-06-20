import streamlit as st
#import yfinance as yf
import pandas as pd
#import plotly.express as px
import datetime
import seaborn as sn
import matplotlib.byplot as plt


# App title
st.markdown('''
# Stock Price App
Shown are the stock price data for query companies!
**Credits**

''')
st.write('---')

# Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2020, 10, 16))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

# Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/regan-mu/ADS-April-2022/main/Assignments/Assignment%201/data.csv')
tickerSymbol = st.sidebar.multiselect('ticker', ticker_list) # Select ticker symbol
tickerDf = ticker_list.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

# Ticker data
st.header('**Ticker data**')
st.write(ticker_list)

# Bollinger bands
st.header('**Bollinger Bands**')
st.title('Stock Price Analysis')
fig=sns.lineplot(x='price', y='date', style='event', data="ticker_list')
st.plot_line(fig);

####
#st.write('---')
#st.write(tickerData.info)
