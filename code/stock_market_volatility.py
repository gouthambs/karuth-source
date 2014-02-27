# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:52:13 2014

@author: Goutham
"""

from pandas.io.data import DataReader
from datetime import date
import matplotlib.pyplot as plt  
import pandas as pd
import math

dfsp        = DataReader('^GSPC','yahoo',date(1980,1,1),date(2013,12,31))

dfsp["Returns"] = dfsp["Adj Close"]/dfsp["Adj Close"].shift(1) - 1
#dfspmon     = dfsp500.resample('M',how='last')
dfsp["Volatility"]  = 100*math.sqrt(252)*pd.rolling_std(dfsp["Returns"],45)

#fig = dfsp[["Volatility","Close"]].plot(subplots=True)
#di = DataReader('IQ12110','fred',datetime.date(1980,1,1),date(2014,1,1))
#ax =plt.gca()
#ax.annotate('Crash',xy=(datetime.date(2008,9,1),41.0),xytext=((datetime.date(2002,9,1),81.0)))

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(dfsp.index, dfsp["Close"],color='k')
axarr[0].set_ylabel("Index Level")
axarr[0].set_title('S&P 500 Index')
axarr[0].grid(True)
axarr[1].plot(dfsp.index,dfsp["Volatility"],color='k')
axarr[1].set_ylabel("Volatility (%)")
axarr[1].set_xlabel("Date")
axarr[1].grid(True)


axarr[0].axvspan(date(1981,7,1), date(1982,11,30), facecolor='g', alpha=0.5)
axarr[0].axvspan(date(1990,7,1), date(1991,3,30), facecolor='g', alpha=0.5)
axarr[0].axvspan(date(2001,3,1), date(2001,11,30), facecolor='g', alpha=0.5)
axarr[0].axvspan(date(2007,12,1), date(2009,6,30), facecolor='g', alpha=0.5)
axarr[0].annotate('Black Monday',xy=(date(1987,10,19),350.0),\
    xytext=((date(1983,10,19),700.0)),arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
axarr[0].annotate('2008 Crash',xy=(date(2008,9,16),1500.0),\
xytext=((date(2002,9,16),1800.0)),arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
                         
axarr[1].axvspan(date(1981,7,1), date(1982,11,30), facecolor='g', alpha=0.5)
axarr[1].axvspan(date(1990,7,1), date(1991,3,30), facecolor='g', alpha=0.5)
axarr[1].axvspan(date(2001,3,1), date(2001,11,30), facecolor='g', alpha=0.5)
axarr[1].axvspan(date(2007,12,1), date(2009,6,30), facecolor='g', alpha=0.5)
axarr[1].annotate('Black Monday',xy=(date(1987,10,19),41.0),\
xytext=((date(1983,10,19),71.0)),arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
axarr[1].annotate('2008 Crash',xy=(date(2008,9,16),41.0),\
xytext=((date(2002,9,16),71.0)),arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
axarr[1].annotate('Downgrade',xy=(date(2011,8,5),41.0),\
xytext=((date(2009,02,16),71.0)),arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))



#dfsp[["Close","Volatility"]].plot(subplots=True)

"""
fig, ax1 = plt.subplots()
ax1.plot(dfsp.index, dfsp["Close"], 'b-')
ax1.set_xlabel('Date')
# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('Index Level', color='b')
ax2 = ax1.twinx()

ax2.plot(dfsp.index,dfsp["Volatility"],'r-')
plt.show()
"""
"""
plt.axvspan(date(1981,7,1), date(1982,11,30), facecolor='g', alpha=0.5)
plt.axvspan(date(1990,7,1), date(1991,3,30), facecolor='g', alpha=0.5)
plt.axvspan(date(2001,3,1), date(2001,11,30), facecolor='g', alpha=0.5)
plt.axvspan(date(2007,12,1), date(2009,6,30), facecolor='g', alpha=0.5)
"""