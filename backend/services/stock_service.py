import yfinance as yf
from stocknews import StockNews
import settings
import pandas as pd

def get_stock(ticker):
    ticker_data = yf.Ticker(ticker)
    return ticker_data

def get_stock_news(ticker):
    sn = StockNews(ticker, wt_key=settings.marketstock_api_key)
    df = sn.read_rss()
    return df

def get_stock_news_title(news_df):
    return news_df.title