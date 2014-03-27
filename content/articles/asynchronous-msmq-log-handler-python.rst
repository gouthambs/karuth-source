Asynchronous Python Logging Using MSMQ
######################################

:date: 2014-02-21
:tags: python, programming
:description: Asynchronous logging in Python using MSMQ. 


If you have a web application running in Python, there can be a need for the logging to
not interfere with the performance. Default file based loggers can lead to a slow down
because of the constand disk writes. An alternate solution that can be quite handy is
logging into a message based logger, such as MSMQ. This post is built on my earlier post
`Sending MSMQ Messages Using Python <|filename|sending-msmq-messages-python.rst>`_, where
I discuss how to setup, send and receive messages using MSMQ.

Here I will show how one can use the MSMQ to build a custom handler, that can be used
with the logging module in python. Here is the ``MSMQHandler`` class:

.. code:: python

	# customhandler.py 
    import logging 

    class MSMQHandler(logging.Handler):
        def __init__(self,queue_name,label_name,dest_computer=None):
            logging.Handler.__init__(self)
            import os
            import win32com.client
            self.queue_name = queue_name
            self.label_name = label_name
            self.computer_name = dest_computer if dest_computer is  None\
                else os.getenv('COMPUTERNAME')
            qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
            qinfo.FormatName="direct=os:"+self.computer_name+\
                "\\PRIVATE$\\"+self.queue_name
            try:
                self.queue = qinfo.Open(2,0)
            except Exception as e:
                self.queue = None
                raise RuntimeError(str(e))

        def emit(self,record):
            import win32com.client
            if self.queue :
                msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
                msg.Label=self.label_name
                msg.Body = self.format(record)
                msg.Send(self.queue)
        
        def close(self)        :
            self.acquire()
            try:
                if self.queue:
                    self.queue.close()
            finally:
                self.release()


Once you have the handler in place, and setup a private MSMQ queue, say KaruthQueue, then
you can incorporate it into your workflow as shown below:

.. code:: python 

    # example.py
    from customhandler import MSMQHandler
    import logging

    lgr = logging.getLogger("Test")            
    hnd = MSMQHandler("KaruthQueue","QPyLog") # here KaruthQueue is the private queue name
    lgr.addHandler(hnd)
    lgr.setLevel(logging.INFO)
    lgr.info("Test Message")
	
And that completes the MSMQ logger using python. Now all your logs will be pushed to the KaruthQueue
that we created. You can use the example shown `here <|filename|sending-msmq-messages-python.rst>`_ to read the messages in a seperate application
and store any way you chose, files, database etc.
