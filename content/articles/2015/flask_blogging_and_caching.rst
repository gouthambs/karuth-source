Adding Caching to Python Flask-Blogging Engine
##############################################

:date: 2015-07-25
:tags: python, flask, programming
:slug: adding-caching-to-python-flask-blogging-extension
:description: This post will discuss caching support to Flask-Blogging
:category: python

I deployed my blogging engine (using `Flask-Blogging extension <https://github.com/gouthambs/Flask-Blogging>`_)
to a site I am building. I am currently hosting the test version on the free instance
of `Openshift <https://openshift.com>`_. So these are not very powerful servers, and
I wasn't expecting any great performance. Here is what I saw while
using Version 0.3.2 of ``Flask-Blogging`::

  $> ab -kc 30 -t 10 https://ucarpool.org/blog/
  
  Benchmarking ucarpool.org (be patient)
  Finished 267 requests
  
  Document Path:          /blog/
  Document Length:        4882 bytes
  
  Concurrency Level:      30
  Time taken for tests:   10.061 seconds
  Complete requests:      267
  Failed requests:        0
  Keep-Alive requests:    267
  Total transferred:      1428480 bytes
  HTML transferred:       1303494 bytes
  Requests per second:    26.54 [#/sec] (mean)
  Time per request:       1130.451 [ms] (mean)
  Time per request:       37.682 [ms] (mean, across all concurrent requests)
  Transfer rate:          138.65 [Kbytes/sec] received
  
  Connection Times (ms)
                min  mean[+/-sd] median   max
  Connect:        0   34  95.5      0     353
  Processing:   272 1040 374.4    936    2166
  Waiting:      267 1037 374.5    933    2163
  Total:        546 1074 349.5    968    2166
  
  Percentage of the requests served within a certain time (ms)
    50%    964
    66%   1039
    75%   1133
    80%   1248
    90%   1812
    95%   1910
    98%   2030
    99%   2070
   100%   2166 (longest request)
   
Thats a measely 26 requests/sec!
  
One of the features I have wanted to add to this extension is the ability to 
cache the pages. Blogs are typically heavy on reads, and light on writes. This
makes an excellent case for caching. 

In order to enable caching support, I am using ``Flask-Cache`` the caching
extension for ``Flask``. The version 0.4.0 of ``Flask-Blogging`` is released with 
caching support built in. ``Flask-Cache`` makes the caching backend 
configurable. It has support for various backends such as filesystem,
redis, and memcache. 

Here is resulting performance after using a filesystem based cache::

  $> ab -kc 30 -t 10 https://ucarpool.org/blog/
  This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
  Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
  Licensed to The Apache Software Foundation, http://www.apache.org/
  
  Benchmarking ucarpool.org (be patient)
  Finished 1815 requests
  
  Document Path:          /blog/
  Document Length:        4882 bytes
  
  Concurrency Level:      30
  Time taken for tests:   10.004 seconds
  Complete requests:      1815
  Failed requests:        0
  Keep-Alive requests:    1815
  Total transferred:      9710280 bytes
  HTML transferred:       8860830 bytes
  Requests per second:    181.43 [#/sec] (mean)
  Time per request:       165.351 [ms] (mean)
  Time per request:       5.512 [ms] (mean, across all concurrent requests)
  Transfer rate:          947.92 [Kbytes/sec] received
  
  Connection Times (ms)
                min  mean[+/-sd] median   max
  Connect:        0    6  44.3      0     400
  Processing:    80  158  46.1    150     411
  Waiting:       79  156  46.1    147     410
  Total:         83  164  58.9    152     518
  
  Percentage of the requests served within a certain time (ms)
    50%    152
    66%    173
    75%    183
    80%    190
    90%    217
    95%    277
    98%    357
    99%    420
   100%    518 (longest request)

Now we are able to serve 180 requests/second. A good 7X performance gain for using a 
filesystem cache. Using in memory like Redis, or SSD filesystem should be even better.

Conclusion
==========

Flask-Blogging, the Flask extension to add Markdown based blog support to Flask sites, incorporates
caching support which has greatly improved its performance.
