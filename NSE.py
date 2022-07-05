import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import datetime
import plotly.graph_objects as go
from dateutil.utils import today
import streamlit as st

st.set_page_config(
    page_title="Nairobi Stock Exchange",
    page_icon="Bar_graph",
    layout="wide",
    initial_sidebar_state="auto",
)
url=("https://raw.githubusercontent.com/regan-mu/ADS-April-2022/main/Assignments/Assignment%201/data.csv")
stock_prices=pd.read_csv(url)
stock_prices.head()
st.sidebar.subheader('Query parameters')
dropdown = st.sidebar.multiselect(
    "Select one ticker:",
    stock_prices["ticker"].unique()
     )

st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2020, 10, 16))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

st.markdown("### Nairobi Stock Exchange")
stock_prices

stock_prices = pd.read_csv("https://raw.githubusercontent.com/regan-mu/ADS-April-2022/main/Assignments/Assignment%201/data.csv")

x = stock_prices['date']
y = stock_prices['price']
fig = px.line(data_frame=stock_prices, y=y, x=x)
st.plotly_chart(fig)

