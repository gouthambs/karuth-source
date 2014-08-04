Running ZEO as a Windows Service
################################

:date: 2014-08-04
:tags: Programming, Python, ZEO, ZODB
:slug: zeo-as-a-windows-service
:author: Gouthaman Balaraman
:description: This article shows how to use ZEO-WinService to run ZEO as a service in Windows.
:keywords: ZEO, ZODB, Python, Programming

The other day, I wanted to run ZEO as a Windows service. The ``runzeo.py`` part of ``ZEO`` will let you
run the client, but it doesn't work well for deployment on a windows machine. So I used ``pywin32`` to wrap
the ``runzeo.py`` into a Windows Service. 


Code
----

You can fetch the source from my github repo_. I do intend to put it on PyPi when I have the time

You can run from ``cmd`` as Administrator::

  > python zeo_winservice.py
  
you will be given the service options, as shown below::


  Usage: 'zeo_winservice.py [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
  Options for 'install' and 'update' commands only:
   --username domain\username : The Username the service is to run under
   --password password : The password for the username
   --startup [manual|auto|disabled|delayed] : How the service starts, default = manual
   --interactive : Allow the service to interact with the desktop.
   --perfmonini file: .ini file to use for registering performance monitor data
   --perfmondll file: .dll file to use when querying the service for
     performance data, default = perfmondata.dll
  Options for 'start' and 'stop' commands only:
   --wait seconds: Wait for the service to actually start or stop.
                   If you specify --wait with the 'stop' option, the service
                   and all dependent services will be stopped, each waiting
                   the specified period.
                   
                   
Installing the Service
----------------------

Before you try to install, make sure you are running ``cmd`` as Administrator.
I like to install such that it will start up automatically, as shown below::

  >python zeo_winservice.py --startup=auto install
  
which gives you the following screen with ZEO options::

  Installing service ZEO WinService
  Start the ZEO storage server.
  
  Usage: %s [-C URL] [-a ADDRESS] [-f FILENAME] [-h]
  
  Options:
  -C/--configuration URL -- configuration file or URL
  -a/--address ADDRESS -- server address of the form PORT, HOST:PORT, or PATH
                          (a PATH must contain at least one "/")
  -f/--filename FILENAME -- filename for FileStorage
  -t/--timeout TIMEOUT -- transaction timeout in seconds (default no timeout)
  -h/--help -- print this usage message and exit
  -m/--monitor ADDRESS -- address of monitor server ([HOST:]PORT or PATH)
  --pid-file PATH -- relative path to output file containing this process's pid;
                     default $(INSTANCE_HOME)/var/ZEO.pid but only if envar
                     INSTANCE_HOME is defined
  
  Unless -C is specified, -a and -f are required.
  
  Enter command line arguments for ZEO Service:
  
Now you are prompted with the different configurations for the ZEO Service that you can pass. One thing to note here
is that the filename option has to absolute path, and not a relative path.

An example command line argument is::

  Enter command line arguments for ZEO Service: -f D:\path\to\data\file.fs -a localhost:9999
  
Here I am specifying that ZEO be run with the ``file.fs`` on ``localhost`` port ``9999``. After installing the
script, you need to start it by::

  >python zeo_winservice.py start
  
You will also be able to access the service from ``task manager`` or the ``Windows Services`` app.


Logging
-------

The logs from the service are sent to the windows ``Event Log`` which can be accessed by opening
the ``Event Viewer``. Once you open the ``Event Viewer``, the logs can be found under::

  Event Viewer->Windows Logs->Application
  
The logs from this script can be found under ``ZEO WinService`` in the Source column.


.. _repo: https://github.com/gouthambs/ZEO-WinService
