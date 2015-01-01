Building Task Pipelines Using Luigi
###################################

:date: 2014-12-31
:tags: Programming, Python, Luigi
:slug: building-luigi-task-pipeline
:author: Gouthaman Balaraman
:description: This is a very basic example on using Luigi as a task pipeline
:keywords: Python, Programming, Luigi, Task Pipeline

It is incredibly easy to write a script to process some data in python. But if you 
have a lot of tasks that depend on each other, and you need to create a robust work 
flow, then thinking in terms of a data pipeline is useful. Luigi is a framework for
building data pipelines, and we will start with a simple "Hello World!" equivalent of
an example. 

Luigi Basics
============

In Luigi, a data pipeline is built by creating ``Task`` objects. For every target, you can define
its dependency by specifying the ``requires`` method for the ``Task``. Every ``Task`` can define 
an ``output`` method to specify where the results of the ``Task`` should go. Lets look at a
simple example to get our feet wet, and gradually build towards complex cases.


Hello World!
============

.. raw:: html

  <script src="https://gist.github.com/gouthambs/873ebce21062914f038d.js"></script>
  
This example is rather self-explanatory. I use the ``MockFile`` class as 
the ``Target`` just so that I can print to console. One can instead use ``luigi.LocalFileTarget(filename)``
to use the file system as the target. The ``main_task_cls`` specifies ``SimpleTask`` as the task
to run. The actual processing part of the task is encapsulated in the ``run`` method of the ``SimpleTask``
class. 

When the script is executed, you should see an output that looks like this::


  DEBUG: Checking if SimpleTask() is complete
  INFO: Scheduled SimpleTask() (PENDING)
  INFO: Done scheduling tasks
  INFO: Running Worker with 1 processes
  DEBUG: Asking scheduler for work...
  DEBUG: Pending tasks: 1
  INFO: [pid 30338] Worker Worker(salt=329921834, host=G-ubuntu, username=myuser, pid=30338) running   SimpleTask()
  SimpleTask: Hello World!
  INFO: [pid 30338] Worker Worker(salt=329921834, host=G-ubuntu, username=myuser, pid=30338) done      SimpleTask()
  DEBUG: 1 running tasks, waiting for next task to finish
  DEBUG: Asking scheduler for work...
  INFO: Done
  INFO: There are no more tasks to run at this time
  INFO: Worker Worker(salt=329921834, host=G-ubuntu, username=myuser, pid=30338) was stopped. Shutting down Keep-Alive thread
  
There you go! You have learnt a basic example.

Linked Task Example
===================

The above example was a good starter example. Though we did not really do much in terms of building a pipeline.
Lets modify the above code a little bit, so we can build a pipeline.

.. raw:: html

  <script src="https://gist.github.com/gouthambs/8740bf4ff5e8269fd56a.js"></script>
  
This example is built on top of the "Hello World" example from above. The ``SimpleTask`` outputs
the text "Hello World!". The ``DecoratedTask`` takes this output from ``SimpleTask`` and prefixes
with the word "Decorated". 

I use the ``MockFile`` here just as a way to see the results on the console. This is 
usually a good testing tool, though I am not sure if it is production ready approach.

The output for the above example would look like::

  DEBUG: Checking if DecoratedTask() is complete
  INFO: Scheduled DecoratedTask() (PENDING)
  DEBUG: Checking if SimpleTask() is complete
  INFO: Scheduled SimpleTask() (PENDING)
  INFO: Done scheduling tasks
  INFO: Running Worker with 1 processes
  DEBUG: Asking scheduler for work...
  DEBUG: Pending tasks: 2
  INFO: [pid 30648] Worker Worker(salt=907129510, host=G-ubuntu, username=myuser, pid=30648) running   SimpleTask()
  SimpleTask: Hello World!
  INFO: [pid 30648] Worker Worker(salt=907129510, host=G-ubuntu, username=v, pid=30648) done      SimpleTask()
  DEBUG: 1 running tasks, waiting for next task to finish
  DEBUG: Asking scheduler for work...
  DEBUG: Pending tasks: 1
  INFO: [pid 30648] Worker Worker(salt=907129510, host=G-ubuntu, username=myuser, pid=30648) running   DecoratedTask()
  DecoratedTask: Decorated Hello World!
  
  INFO: [pid 30648] Worker Worker(salt=907129510, host=G-ubuntu, username=myuser, pid=30648) done      DecoratedTask()
  DEBUG: 1 running tasks, waiting for next task to finish
  DEBUG: Asking scheduler for work...
  INFO: Done
  INFO: There are no more tasks to run at this time
  INFO: Worker Worker(salt=907129510, host=G-ubuntu, username=myuser, pid=30648) was stopped. Shutting down Keep-Alive thread

Conclusion
==========

Here we learnt a really basic example that gives you basic idea on building Luigi based pipelines.
