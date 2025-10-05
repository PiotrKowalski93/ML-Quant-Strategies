from statsmodels.regression.rolling import RollingOLS
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import pandas_ta as ta
import warnings
warnings.filterwarnings('ignore')

## Importing list of stocks
# stocks_symbols = pd.read_csv("./symbols_sp500.csv")['Symbol']
# stocks_symbols = stocks_symbols.str.replace('.', '-')

# end_date = '2025-10-05'
# start_date = pd.to_datetime(end_date) - pd.DateOffset(365*8)

# symbol_list = stocks_symbols.unique().tolist()

# df = yf.download(tickers=symbol_list,
#                  start=start_date,
#                  end=end_date,
#                  auto_adjust=False).stack()

# df.index.names = ['date', 'ticker']
# df.columns = df.columns.str.lower()

# # Save to file, to not dowload it every time
# df.to_csv('./stocks_data_frame.csv')

# ## Read saved data
df = pd.read_csv('./stocks_data_frame.csv')
print(df)

## Garman-Klass Volatility
df['garman_klass_vol'] = ((np.log(df['high'])-np.log(df['low']))**2)/2 - (2*np.log(2)-1)*((np.log(df['adj close'])-np.log(df['open']))**2)

## RSI

## Bollinger Bands

## ATR

## MACD

## Dollar Volume
