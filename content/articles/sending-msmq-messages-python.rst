Sending MSMQ Messages Using Python
##################################
:date: 2014-02-21
:tags: python, programming
:description: Send MSMQ messages using python

Here I show how to send and receive MSMQ messages using python. 

Setting Up MSMQ on Windows 7
----------------------------
Before we can proceed with the code, here is a quick note on set-up. 
To setup MSMQ (disabled by default) go to *Control Panel* -> *Programs and Features* -> *Turn Windows Features on or off* (on the left panel). Now check *Microsoft Message Queue(MSMQ) Server* if it is not checked. Hit OK. Now we have enabled MSMQ server.

Now that we have the MSMQ server up and running, lets create a private queue so we can use in our script. To do that, go to *Control Panel* -> *Administrative Tools* -> *Computer Management*. Expand *Services and Applications* -> *Message Queuing*. Select *Private Queues* under *Message Queuing* and right-click and click *New*. Now in the dialog box put a *Queue Name*, for this example purpose, say *KaruthQueue* and click OK.

Installing PyWin32
------------------

To send and receive MSMQ messages you need the awesome Python for Windows Extension module, PyWin32_ by Mark Hammond. Once you have completed installation, you can check if your installation is fine by trying ``import win32com``. If you don't get any errors, then you are good to go.

Sending MSMQ Messages
---------------------

Here is a small code snippet that shows you how to send messages using MSMQ.

.. code:: python

	import win32com.client
	import os	

	qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
	computer_name = os.getenv('COMPUTERNAME') 
	qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\KaruthQueue"  
	queue=qinfo.Open(2,0)   # Open a ref to queue
	msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
	msg.Label="TestMsg"
	msg.Body = "The quick brown fox jumps over the lazy dog"
	msg.Send(queue)
	
	queue.Close()

Voila! We have sent our message. You can check if the message was sent properly by checking under
*Control Panel* -> *Administrative Tools* -> *Computer Management* -> *Services and Applications* -> *Message Queuing* -> *Private Queues*
-> *KaruthQueue* -> *Queue Messages*. Right click and refresh after you have run the script, if you don't see any.
You should see an entry there that corresponds to the message that was sent 


Receiving MSMQ Messages
-----------------------

.. code:: python

	import win32com.client
	import os

	qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
	computer_name = os.getenv('COMPUTERNAME') 
	qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\KaruthQueue"  
	queue=qinfo.Open(1,0)   # Open a ref to queue to read(1)
	msg=queue.Receive()
	print "Label:",msg.Label
	print "Body :",msg.Body
	queue.Close()
	
Run this code after you have sent the message using the above script. Now you should 
see your earlier message printed out.

Have fun messaging!

.. _PyWin32 : http://sourceforge.net/projects/pywin32/
