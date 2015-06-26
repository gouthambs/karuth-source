Title:  How to Build a Fundamental Factor Model
Slug: build-fundamental-factor-model
Date: 2015-06-22
Category: finance
Tags: finance
Author: Gouthaman Balaraman
Description: This post outlines the methodology behind building a fundamental factor model.




In a multi-factor model, the return of a stock can be broken out 
into multiple factors.

$$ r_i = \\alpha_i + \\sum_{j=1}{K} \\beta_{ij} f_j + \\epsilon_i $$

The term $\\epsilon_i$ is the error term which is assumed to have a 
distribution with zero mean. Now we can write the average return as

$$ E(r_i) = E(\\alpha_i) + \\sum_{j=1}{K} \\beta_{ij} E(f_j) $$

This can be expressed concisely using the matrix representation:

$$ r_i = \\mathbf{\\beta}^T_i \\mathbf{f}  + \\epsilon_i $$

where:

\begin{eqarray}
\mathbf{\\beta}_i &=& (\\alpha_i, \\beta_{i1}, \\beta_{i2}, ..., \\beta_{iK})^T \\ 
\mathbf(f) &=& (1, f_1, f_2, ..., f_K)^T
\end{eqarray}

Using this notation, the average return can then be written as:

$$ E(r_i) = \\mathbf{\\beta}_i^T E(\\mathbf{f}) $$

We see that the average return on the stock is the product of factor exposures ($\\mathbf{\\beta}_i$) and factor premium ($\\mathbf{f}$). In a fundamental factor model, the *factor exposures*  are characteristics of an investment (such as a stock) that is known, such as the Price to Earnings ratio, or momentum of the stock, or market capitalization. The *factor premium* is the unknown that we wish to determine empirically. 

One of the tenets of quantitative portfolio management is:
*the average return of an investment is the payoff
for taking risk*. The risk of a stock has two components:

Total Risk = Non-Diversifiable Risk + Diversifiable Risk

Risk can be measured using the variance of the returns:

$$ V(r_i) = V(\\alpha + \\beta_{i1}f_1 + ... + \\beta_{iK}f_K) + V(\\epsilon_i) + V(\\epsilon_i)$$.

This can be expressed in the matrix notation as:

$$ V(r_i) = \\mathbf{\\beta}_i^T V(\\mathbf{f}) \\mathbf{\\beta}_i + V(\\epsilon_i) $$

where $V(\\mathbf{f})$ is a $(K+1) \times (K+1)$-dimensional variance-covariance matrix. The diversifiable component which an investor can mitigate by diversification
is the term $V(\\epsilon_i)$. The non-diversifiable componenent which the market 
rewards is obtained from factor exposures $\\mathbf{\\beta}_i$ and factor premium
risk $V(\\mathbf{f})$.


## Preparatory Work

There are a series of steps that one has to do before we can run a 
multi-variable regression to determine the factor premiums. 

### Choosing the factors

We need to choose the factors that we wish to include in the model. This step 
is usually driven by the intuition an investor has on the market, and 
characteristics of the stock that are important. For instance, some fundamental factors that would make sense for equity investments include:

1. *Valuation Factors*: Market capitalization (size), price-to-book ratio (P/B),
price-to-earnings ratio (P/E), price-to-sales ratio (P/S).
2. *Solvency Factors*: Debt-to-equity ratio (D/E), current ratio (CUR, a metric
of short term solvency), interest coverage ratio.
3. *Growth Potential Factors*: Capital-expenditure-to-sales ratio, R&D-expenditure-to-sales ratio, advertising-expenditure-to-sales ratio.
4. *Technical factors*: Momentum, trading volume, short interest shares shorted
5. *Analyst factors*: Analyst rating changes, earnings revision etc.

Similarly some fundamental factors that would make sense for fixed income investments 
include:

1. *Credit Factors*: Credit quality, different vendor ratings
2. *Interest Rate Sensitivity Factors*: Effective duration, key rate duration at
various tenors, convexity
3. *Asset Type Factors*: Some factors can be asset specific, such as:
	1. *Municipals*: 
		1. State or issuer
		2. Purpose such as revenue or general obligation
	2. *Mortgages*:
		1. Coupon
		2. Amortization type
		3. Issuer

### Treatment of the Risk-Free Rate

Since we are building a model to measure the payoff for undertaking risk, it is
conventional to subtract the risk-free rate from the returns of the investment. The
rational is that the risk-free rate is the return that can be obtained on any
investment without any risk. In order to do this, we need to define what is
considered risk-free. In the U.S. markets, the U.S. treasury bills are used
as a proxy for the risk free rate. In other markets, one has to exercise care
in identifying a risk free rate. All sovereign bond/bill  rates do not 
immediately translate into risk-free rates because a lot of countries (developing 
and developed) have risk of default as well. 

Once the risk-free rate $r_{ft}$ has been identified, the excess return can be defined
as 

$$ \\hat{r}_{it} = r_{it} - r_{ft} $$

### Building the Data Sample

One of the crucial components in the factor model building process is 
to create a data sample that can then be used to deduce the model 
parameters. For example, to model the U.S. equity market one can use
the top 2000 to 3000 stocks by market cap. Depending on where we cutoff, 
this will include stocks in the large-cap and mid-cap range. This would mean
that the model may not precisely model the effects in the small-cap stocks.
On the other hand, limiting to stocks in the mid-cap or large-cap range can
provide more stability to the model, and that could be a desirable thing.  

Once we have a filter for deciding how we want to build the basket of 
instruments for model building, we also have to decide the frequency and 
period for which we need to collect the data. What do we mean by that? The
regression step involved in the model building will fit the stock returns
$r_{it}$ for a period (such as one day returns or monthly returns) as 
a function of various factors $f$. The return data is collected over multiple
periods, such as 3 years or 5 years. For instance, our data sample could
be top 3000 stocks by market cap with monthly returns collected for 3 years.
A rule of thumb is that the frequency of the investor's re-balancing strategy
should determine the frequency of the returns used in the model building.
If the re-balances  monthly, then one should use monthly returns in the 
model fitting. There should be sufficient time periods included in order
to avoid spurious fitting effects and to improve robustness of fit. 
It is conventional to use 3 to 5 years worth of data while using monthly 
returns, and 2 to 3 years while using weekly returns.  

Another factor that one should keep in mind is to include companies
that are not only alive at the time of model building but also to include
companies that may have gotten delisted or bankrupt. Failure to do 
so will introduce what is called as *survivorship bias* in your model. 

## Fitting the Model

Once we have the data sample assembled, one can use regression utilities
in statistical packages such as *R*, Python's *Statsmodels* package, *Matlab*,
SAS to perform a panel regression. The goal of the panel regression is 
to estimate factor premium $\\mathbf{f}$ given by the equation 

$$ r_i = \\mathbf{\\beta}^T_i \\mathbf{f}  + \\epsilon_i $$

where the returns $r_i$ and the factor exposures $\\mathbf{\\beta}_i$
are known. A simple way to estimate factor premiums is by using 
Ordinary Least Squares (OLS). This will also give us an estimate
of the variance matrix $V(\\mathbf{\\hat{f}}$.

## Robustness Considerations

It is important that the estimates of the factor premium and 
the variance of factor premiums are fairly robust. 

## Conclusions

## Further Reading


... to be continued








 
