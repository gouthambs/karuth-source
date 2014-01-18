# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:52:13 2014

@author: Goutham
"""

from pandas.io.data import DataReader
from datetime import date
import matplotlib.pyplot as plt  
import pandas as pd

dfsp        = DataReader('MT','yahoo',date(1950,1,1),date(2013,12,31))
dfsp["Returns"] = dfsp["Adj Close"]/dfsp["Adj Close"].shift(1) - 1
#dfspmon     = dfsp500.resample('M',how='last')
dfsp["Volatility"]  = sqrt(252)*pd.rolling_std(dfsp["Returns"],45)

dfsp[["Volatility","Close"]].plot(subplots=True)