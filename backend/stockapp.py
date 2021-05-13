import datetime

import streamlit as st


# sidebar input box
from backend.services.stock_service import get_stock, get_stock_news, get_stock_news_title

ticker = st.sidebar.text_input('Please enter a ticker')
time_period_start = st.sidebar.date_input("start from", datetime.date.today())
time_period_end = st.sidebar.date_input("end with", datetime.date.today())

stock_df = get_stock(ticker)
stock_hist = stock_df.history(period='1d', start=time_period_start, end=time_period_end)

stock_news = get_stock_news(ticker)
stock_news_title = get_stock_news_title(stock_news)
if stock_hist.empty:
    st.error('PLease finish the configuration on the left')
else:
    stock_info = stock_df.info['longBusinessSummary']
    st.write(stock_info)
    st.dataframe(stock_hist)
    st.write(stock_news)
    st.write(stock_news_title)
