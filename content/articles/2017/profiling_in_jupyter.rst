Profiling Python Code in Jupyter Notebooks
##########################################

:author: Goutham Balaraman
:date: 2017-03-02
:slug: profiling-python-jupyter-notebooks
:tags: Python, Jupyter, Programming
:description: Some notes on profiling python code in the Jupyter notebook environment

Sometimes you want to quickly identify performance bottlenecks in your code. You can use some of these recipes while 
using the Jupyter notebook environment. Jupyter allows a few magic commands that are great for timing and profiling a line of 
code or a block of code. Let us take a look at a really simple example with these functions:

.. code:: python

  import numpy as np
  
  def func(n, a):
    y = np.arange(n)
    y = np.exp(-y*a)
    return y
    
  def gunc(n, a):
    y = np.exp(-n*a)
    return y
    
  def hunc(n, a):
    y1 = func(n, a)
    y2 = gunc(n, a)
    return y1, y2
    
    
    
**timeit**

Now to see which one of these is faster, you can use the ``%timeit`` magic command:
 
.. code:: python
 
   %timeit -n 3 func(10,0.5)
   
   
``3 loops, best of 3: 14.1 µs per loop``


Here the ``-n 3`` denotes the number of loops to execute. The default is 100000 loops. Now let's say you have 
both ``func`` and ``gunc`` in a cell, and you want to measure the time taken, then you can use ``%%timeit`` in the
block. Notice the double percentage sign:

.. code:: python

  %%timeit -n 3
  func(10, 0.5)
  gunc(10, 0.5)


``3 loops, best of 3: 18.2 µs per loop``



**time**

On some occasions, you can get the time taken using the ``%time`` magic command for the line or ``%%time`` for the cell block.:

.. code:: python

  %%time
  func(60000, 0.5)
  gunc(10, 0.5)
  
  
``Wall time: 10 ms``
  
  

**prun**

The above recipes are more of timing code than profiling code. There is a profiler magic command ``%prun`` and ``%%prun`` that
does function level code profiling. For example


.. code:: python

  %prun hunc(50000, 0.5)
  

::


  7 function calls in 0.010 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.009    0.009    0.009    0.009 <ipython-input-23-5c434cf7f3ad>:3(func)
        1    0.001    0.001    0.001    0.001 {built-in method numpy.core.multiarray.arange}
        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 <ipython-input-23-5c434cf7f3ad>:8(gunc)
        1    0.000    0.000    0.009    0.009 <ipython-input-23-5c434cf7f3ad>:12(hunc)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} 
        


**lprun**

Lastly, you can install the ``line_profiler`` if you want to dig a little deep to understand what line in the code is slow.
You can install as::

  pip install line_profiler
  
This extension  be loaded as::

  %load_ext line_profiler
  
Let's say we have a hunch that the ``func`` call in ``hunc`` is the bottleneck, but we are wondering which line in ``func`` is 
the culprit, then here is how ``%lprun`` can help.

.. code:: python

  %lprun -f func hunc(50000, 0.5)
  
  
::

  Timer unit: 3.00459e-07 s

  Total time: 0.00950652 s
  File: <ipython-input-23-5c434cf7f3ad>
  Function: func at line 3

  Line #      Hits         Time  Per Hit   % Time  Line Contents
  ==============================================================
       3                                           def func(n, a):
       4         1         1288   1288.0      4.1      y = np.arange(n)
       5         1        30340  30340.0     95.9      y = np.exp(-y*a)
       6         1           12     12.0      0.0      return yTimer unit: 3.00459e-07 s


If you need to profile some function in a python package, then import that function and stick it after ``-f`` flag. Happy profiling!
