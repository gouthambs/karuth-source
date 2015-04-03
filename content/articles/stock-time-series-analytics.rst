Calculating Stock Beta, Volatility, and More
############################################

:date: 2014-1-9
:tags: finance, investing
:slug: calculating-stock-beta
:author: Gouthaman Balaraman
:description: Introduction to calculating Beta, Alpha and R-squared for a stock. This article
 will also include a python code snippet to calculate these measures. This method is for instance
 used by sites like yahoo to show beta, volatility etc.
  
:keywords: investment, stock, beta
	
 
Have you ever wondered how to calculate the Beta value that is shown in 
GoogleFinance_ or YahooFinance_ and what does it mean from an investment perspective? 
This article will give you an introduction to the concept and demonstrate how
you can calculate various time series measures for a stock using python. The 
`Modern Portfolio Theory Statistics </blog/modern-portfolio-theory-statistics.rst>`_
page shows calculated betas, alpha, etc for a few thousand stocks.

Beta, Alpha and R-squared
-------------------------
Beta of a stock is a measure of relative risk of the stock with respect to the market.
The convention (though not a rule) is to use S&P 500 index as the proxy for market. 
A beta value of greater than 1 means that the stock returns amplify the market returns
on both the upside and downside. On the contrary, a beta value of less than 1 means 
that the stock returns are subdued in comparison to the market returns.
It is very important to understand that beta is a relative measure of risk, and 
not an absolute measure of risk. That means that we are only saying how risky the stock is
vis-a-vis the market. If the stock market itself is overheated and volatile, then
a beta of 1 means that the stock is equally volatile, and equally risky.

The beta is calculated using regression analysis. In simple terms if you plot
the returns of stock as a function of the returns of the market benchmark (such as S&P 500) 
and fit it with a straight line, then beta is nothing but the slope of the fitted line. 
The regression equation is given as shown below.

$$ R^{stock}_i = \\alpha + \\beta \\times R^{market}_i + \\epsilon_i  $$
	
In Capital Asset Pricing Model, the returns of the stock $R^{stock}$
and that of the market $R^{market}$ are adjusted for the risk-free
rate. Here for simplicity I leave that out. Given the current low interest rate 
environment, this adjustment will add little value.

Alpha of a stock gives you a measure of the excess return with respect to the benchmark.
A positive alpha for a stock or portfolio gives you sense of how well your asset
outperformed a benchmark. 

The $R^2$ is a measure of how well the the returns of a stock is explained by the 
returns of the benchmark. If your investment goal is to track a particular benchmark,
then you should chose stocks that show a high $R^2$ with respect to the benchmark.
The $R^2$ value of $1$ means that the benchmark completely explains the stock returns, 
while a value of $0$ means that the benchmark does not explain the  stock
returns.

R-squared is defined as:

$$    R^2 = 1 - SS_{res}/SS_{tot} $$

where 


$$    SS_{res} = \\sum_i (R^{stock}_i - f^{stock}_i)^2 $$

$$    SS_{tot} = \\sum_i (R^{stock}_i - <R^{stock}>)^2 $$


Volatility and Momentum
-----------------------

The measures discussed in the earlier section are what I would call *relative 
measures*, i.e., they are with respect to a proxy that is a representation of 
market. Time series measures such as volatility and momentum are what I would
call *innate measures*. 

Volatility is nothing but the standard deviation of the returns of the stock.
It gives us a sense of how much the stock returns fluctuate and how risky it is.
High volatile stocks have high risk, and also have the potential to offer higher
returns. A 3-year history of 1-month returns can be a good sample to calculate
volatility. 

Momentum is a measure of the past returns over a certain period. The 1-year 
momentum will be the 1-year return of the stock, where as a 3-year momentum
will be the 3-year return of the stock.




Python Code
-----------

One can use data from yahoo finance to calculate the stock beta as shown:

.. code:: python

    from pandas.io.data import DataReader
    from datetime import date
    import numpy as np
    import pandas as pd
    	
    # Grab time series data for 5-year history for the stock (here AAPL)
    # and for S&P-500 Index
    sdate = date(2008,12,31)
    edate = date(2013,12,31)
    df = DataReader('WFM','yahoo',sdate,edate)
    dfb = DataReader('^GSPC','yahoo',sdate,edate)
    	
    # create a time-series of monthly data points 
    rts = df.resample('M',how='last')
    rbts = dfb.resample('M',how='last')
    dfsm = pd.DataFrame({'s_adjclose' : rts['Adj Close'],
                            'b_adjclose' : rbts['Adj Close']},
                            index=rts.index)
    
    # compute returns
    dfsm[['s_returns','b_returns']] = dfsm[['s_adjclose','b_adjclose']]/\
        dfsm[['s_adjclose','b_adjclose']].shift(1) -1
    dfsm = dfsm.dropna()    	
    covmat = np.cov(dfsm["s_returns"],dfsm["b_returns"])
    
    # calculate measures now
    beta = covmat[0,1]/covmat[1,1]
    alpha= np.mean(dfsm["s_returns"])-beta*np.mean(dfsm["b_returns"])
    
    # r_squared     = 1. - SS_res/SS_tot
    ypred = alpha + beta * dfsm["b_returns"] 
    SS_res = np.sum(np.power(ypred-dfsm["s_returns"],2))
    SS_tot = covmat[0,0]*(len(dfsm)-1) # SS_tot is sample_variance*(n-1) 
    r_squared = 1. - SS_res/SS_tot
    # 5- year volatiity and 1-year momentum
    volatility = np.sqrt(covmat[0,0])
    momentum = np.prod(1+dfsm["s_returns"].tail(12).values) -1
    
    # annualize the numbers
    prd = 12. # used monthly returns; 12 periods to annualize
    alpha = alpha*prd
    volatility = volatility*np.sqrt(prd)
    
    print beta,alpha, r_squared, volatility, momentum

    
Some caveats about the sample code. The returns are calculated using the 
adjusted close from Yahoo finance data. This is because the adjusted close
accounts for dividends and splits etc. In my personal experience I have
found the returns calculated this way to be a reasonably close estimate 
but not always accurate. The volatility is calculated here as a simple
standard deviation of the returns. From an option-pricing
model perspective volatility is calculated assuming a log-normal distribution
for the returns.

The alpha shown above is annualized by scaling by a factor of 12, the periodicity
of returns. The same goes for volatility, which is scaled by $\\sqrt{12}$
in order to annualize.

    


.. _GoogleFinance:  http://www.google.com/finance
.. _YahooFinance: http://www.finance.yahoo.com/
