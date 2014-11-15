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
  
- Add to /etc/hosts. In your *desktop*, associate the linode IP with a custom servername of
  your liking. Edit /etc/hosts to look like::
  
    
    127.0.0.1	localhost
    127.0.1.1	G-ubuntu
    111.11.11.1 ServerName
    
  Also on you linode add an entry to associate ``127.0.0.1`` with the server hostname. If not you will
  a error message that the <ServerName is not recognized when you ``sudo``. Add the following to /etc/hostname
  in your linode::
  
    127.0.0.1  ServerName

Securing Linode
---------------

- Setting up firewall: When I type ``sudo iptables -L`` I get::

    Chain INPUT (policy ACCEPT)
    target     prot opt source               destination
    
    Chain FORWARD (policy ACCEPT)
    target     prot opt source               destination
    
    Chain OUTPUT (policy ACCEPT)
    target     prot opt source               destination

  Now create a file to store the firewall rules using ``sudo nano /etc/iptables.firewall.rules`` and 
  paste the following::
  
    *filter
    
    #  Allow all loopback (lo0) traffic and drop all traffic to 127/8 that doesn't use lo0
    -A INPUT -i lo -j ACCEPT
    -A INPUT -d 127.0.0.0/8 -j REJECT
    
    #  Accept all established inbound connections
    -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    
    #  Allow all outbound traffic - you can modify this to only allow certain traffic
    -A OUTPUT -j ACCEPT
    
    #  Allow HTTP and HTTPS connections from anywhere (the normal ports for websites and SSL).
    -A INPUT -p tcp --dport 80 -j ACCEPT
    -A INPUT -p tcp --dport 443 -j ACCEPT
    
    #  Allow SSH connections
    #
    #  The -dport number should be the same port number you set in sshd_config
    #
    -A INPUT -p tcp -m state --state NEW --dport 22 -j ACCEPT
    
    #  Allow ping
    -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
    
    #  Log iptables denied calls
    -A INPUT -m limit --limit 5/min -j LOG --log-prefix "iptables denied: " --log-level 7
    
    #  Drop all other inbound - default deny unless explicitly allowed policy
    -A INPUT -j DROP
    -A FORWARD -j DROP
    
    COMMIT
  
  Now the firewall rules can be activated using::
  
    sudo iptables-restore < /etc/iptables.firewall.rules
    
  Now when you type ``sudo iptables -L``::
  
    Chain INPUT (policy ACCEPT)
    target     prot opt source               destination
    ACCEPT     all  --  anywhere             anywhere
    REJECT     all  --  anywhere             127.0.0.0/8          reject-with icmp-port-unreachable
    ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:http
    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:https
    ACCEPT     tcp  --  anywhere             anywhere             state NEW tcp dpt:ssh
    ACCEPT     icmp --  anywhere             anywhere
    LOG        all  --  anywhere             anywhere             limit: avg 5/min burst 5 LOG level debug prefix "iptables denied: "
    DROP       all  --  anywhere             anywhere
    
    Chain FORWARD (policy ACCEPT)
    target     prot opt source               destination
    DROP       all  --  anywhere             anywhere
    
    Chain OUTPUT (policy ACCEPT)
    target     prot opt source               destination
    ACCEPT     all  --  anywhere             anywhere 

  Now to ensure that the firewall is going to be up and running every time you reboot your
  Linode, edit ``/etc/network/if-pre-up.d/firewall`` as ``sudo`` to add::

    #!/bin/sh
    /sbin/iptables-restore < /etc/iptables.firewall.rules
    
  Once you have saved these edits, make this file executable using::
  
    sudo chmod +x /etc/network/if-pre-up.d/firewall
  
  This should secure your server. If you want to make sure your firewall is up and running,
  reboot the server and check what you get when you type ``sudo iptables -L``.

- Installing and Configuring Fail2Ban: Fail2Ban is an application that prevents 
  dictionary attacks on your server. When Fail2Ban detects multiple failed login 
  attempts from the same IP address, it creates temporary firewall rules that block 
  traffic from the attacker’s IP address. Attempted logins can be monitored on a 
  variety of protocols, including SSH, HTTP, and SMTP. By default, Fail2Ban monitors SSH only.

  Here’s how to install and configure Fail2Ban:

  - Install Fail2Ban by entering the following command::
      
      sudo apt-get install fail2ban
    
  Optionally, you can override the default Fail2Ban configuration by creating 
  a new ``jail.local`` file. Enter the following command to create the file::
    
    sudo nano /etc/fail2ban/jail.local
    
  To learn more about Fail2Ban configuration options, see this article on the Fail2Ban_ website.
  Fail2Ban is now installed and running on your Linode. It will monitor your log files for failed 
  login attempts. After an IP address has exceeded the maximum number of authentication attempts, 
  it will be blocked at the network level and the event will be logged in ``/var/log/fail2ban.log``.


Python Setup
------------

- 


.. _Fail2Ban:  http://www.fail2ban.org/wiki/index.php/MANUAL_0_8#Configuration
