An Introduction to Interest Rate Term Structure in QuantLib
###########################################################

:date: 2015-03-28
:tags: python, finance, quantlib
:slug: quantlib-term-structure
:description: This post will walk through the basics of constructing an interest rate term structure in QuantLib.


Term structure is pivotal to pricing securities. One has to know how to create a ``YieldTermStructure`` object
in QuantLib to use the pricing engines. Here I will give an overview of how to create an interest rate
term structure.

The examples I found on QuantLib term structures discuss bootstrapping from treasury bills, notes and bonds.
Such an exercise is required when you are constructing the curve yourself.

