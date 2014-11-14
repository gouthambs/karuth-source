Setting Up Linode For The Impatient
###################################

:date: 2014-11-13
:tags: programming, linux
:slug: setting-up-linode
:author: Gouthaman Balaraman
:description: Some notes based on my experience setting up the linode server

When you get a linode instance, you really get a barren (sort of) linux machine on the cloud. That means 
you have to take care of customizing the server based on your needs. Here are some notes based on what I 
wanted to setup.

My requirements were the following:

- Python Setup: Setup python to perform installations using ``pip``.
- Secure Server: Enable firewall etc.

Linode Basics
-------------

- Once I setup the linode account, I used the ssh instructions on the "Remote Access" in the linode
  dashboard to get the IP as::

    ssh root@<ip-address>

- Setup hostname::
    
    echo "ServerName" > /etc/hostname
    hostname -F /etc/hostname

  Try ``hostname`` on the command line to see the hostname printed correctly.

Python Setup
------------

