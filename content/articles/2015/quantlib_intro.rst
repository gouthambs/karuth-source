QuantLib Basics
###############

:date: 2015-03-24
:tags: python, finance, quantlib
:slug: quantlib-basics
:description: This post will walk through some of the basics of QuantLib library.


I installed the latest version of QuantLib (V1.5) and the python wrapper to QuantLib.
My experiments lately have been to get a feel for the QuantLib API. The library itself
is so extensive, that it is rather hard for a new comer to get going. In this post
we will look into some of the basic classes and functionality in QuantLib.

Let us import QuantLib as:

.. code:: python

    import QuantLib as ql


Time SubModule
==============

The ``ql/time`` sub-folder implements various time related classes. Lets take a look
at the ``Date`` object which can be constructed as ``Date(date, month, year)``.

.. code:: python


    >>> date = ql.Date(31, 3, 2015) # 31 March, 2015
    >>> print date
    March 31st, 2015
    >>> date.dayOfMonth()
    31
    >>> date.month()
    3
    >>> date.year()
    2015
    >>> date.weekday() == ql.Tuesday
    True

    # arithmetic with dates
    >>> date + 1  # add a day
    Date(1,4,2015)
    >>> date - 1  # subtract a day
    Date(30,3,2015)
    >>> date + ql.Period(1, ql.Months)
    Date(30,4,2015)
    >>> date + ql.Period(1, ql.Weeks)
    Date(7,4,2015)
    >>> date + ql.Period(1, ql.Years)
    Date(31,3,2016)

    # logical operations
    >>> ql.Date(31, 3, 2015) > ql.Date(1, 3, 2015)
    True


The ``Schedule`` object can be used to construct a list of dates such as coupon payments.
Lets look at some examples.

.. code:: python

    >>> date1 = ql.Date(1, 1, 2015)
    >>> date2 = ql.Date(1, 1, 2016)
    >>> tenor = ql.Period(ql.Monthly)
    >>> calendar = ql.UnitedStates()
    >>>
    >>> schedule = ql.Schedule(date1, date2, tenor, calendar, ql.Following,
                               ql.Following, ql.DateGeneration.Forward, False)
    >>> list(schedule)
    [Date(2,1,2015),
     Date(2,2,2015),
     Date(2,3,2015),
     Date(1,4,2015),
     Date(1,5,2015),
     Date(1,6,2015),
     Date(1,7,2015),
     Date(3,8,2015),
     Date(1,9,2015),
     Date(1,10,2015),
     Date(2,11,2015),
     Date(1,12,2015),
     Date(4,1,2016)]

Here we have generated a ``Schedule`` object that will contain dates between ``date1`` and ``date2`` with the
``tenor`` specifying the ``Period`` to be every Month. The ``calendar`` object is used for determining holidays.
The two arguments following the ``calendar`` in the ``Schedule`` constructor are the ``BussinessDayConvention``.
Here we chose the convention to be the day following holidays. That is why we see that holidays are excluded
in the list of dates.

Conclusion
==========

In this post we looked at the basics of QuantLib, more specifically the time module. We learnt to
create ``Date`` objects and ``Schedules``.







