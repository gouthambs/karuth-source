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
$$ r_i = \\mathbf{\\beta}^T_i \\mathbf{f}  + \epsilon_i $$
where:

\begin{eqarray}
\mathbf{\\beta}_i &=& (\\alpha_i, \\beta_{i1}, \\beta_{i2}, ..., \\beta_{iK})^T \\ 
\mathbf(f) &=& (1, f_1, f_2, ..., f_K)^T
\end{eqarray}

Using this notation, the average return can then be written as:
$$ E(r_i) = \\mathbf{\\beta}_i^T E(\\mathbf{f}) $$
We see that the average return on the stock is the product of factor
exposures ($\\mathbf{\\beta}_i$) and factor premium ($\\mathbf{f}$). 
In a fundamental factor model, the *factor exposures*  are characteristics 
of an investment (such as a stock) that is known, such as the Price to 
Earnings ratio, or momentum of the stock, or market capitalization. 
The *factor premium* is the unknown that we wish to determine empirically. 

One of the tenets of quantitative portfolio management is:
*the average return of an investment is the payoff
for taking risk*. So what is the risk associated with 
this average return? The risk of a stock has two components:

Total Risk = Non-Diversifiable Risk + Diversifiable Risk

Risk can be measured using the variance of the returns:
$$ V(r_i) = V(\\alpha + \\beta_{i1}f_1 + ... + \\beta_{iK}f_K) + V(\\epsilon_i) + V(\\epsilon_i)$$.
This can be expressed in the matrix notation as:
$$ V(r_i) = \\mathbf{\\beta}_i^T V(\\mathbf{f}) \\mathbf{\\beta}_i + V(\\epsilon_i) $$
where $V(\\mathbf{f})$ is a $(K+1) \times (K+1)$-dimensional variance-covariance matrix. 
The diversifiable component which an investor can mitigate by diversification
is the term $V(\\epsilon_i)$. The non-diversifiable componenent which the market 
rewards is obtained from factor exposures $\\mathbf{\\beta}_i$ and factor premium
risk $V(\\mathbf{f})$.


 



... to be continued








 
