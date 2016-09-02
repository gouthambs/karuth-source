Minimal Flask-Login Example
###########################


:date: 2014-07-24
:tags: Programming, Python, Flask, Authentication
:slug: minimal-flask-login-example
:author: Gouthaman Balaraman
:description: Flask-Login is a Flask extension that provides a framework for handling user authentication. 
 This post will give you a basic tutorial of the Flask-Login mechanism for token based authentication.
:keywords: Flask, Python, Programming, Analytics, Authentication, Flask-Login, Flask Login


The goal of this post is to give a very basic introduction to token based authentication using Flask-Login. 
Usually the user credentials are stored in a database, with passwords hashed. However the authentication 
mechanism can be understood without having to worry about database, and various token generation algorithms.
As a first step lets focus on just understanding the authentication mechanism. Then in a subsequent post
we will handle other important parts.


To run this example, you will need `flask` and `flask-login` with their dependencies installed.
This can be done using `pip` as shown below::
  
  >pip install flask
  >pip install flask-login
  

Example Code
------------

Here is the full source code that we are about to discuss:

.. raw:: html   

 <script src="https://gist.github.com/gouthambs/0a509faf231cff3cdec7.js"></script>


Code Explained
--------------

Lets delve deeper into this example, and I will explain each part of the code in greater detail here.


.. code:: python

  from flask import Flask, Response
  from flask.ext.login import LoginManager, UserMixin, login_required
  
  app = Flask(__name__)
  login_manager = LoginManager()
  login_manager.init_app(app)
  

The first five lines of the code import the required modules, and initializes the Flask ``app``. Then
the `LoginManager` instance is created and then is configure for login. Now lets try to understand
the `User` class.

.. code:: python

  class User(UserMixin):
      # proxy for a database of users
      user_database = {"JohnDoe": ("JohnDoe", "John"),
                 "JaneDoe": ("JaneDoe", "Jane")}
      
      def __init__(self, username, password):
          self.id = username
          self.password = password
          
      @classmethod
      def get(cls,id):
          return cls.user_database.get(id)
          
          
Here I have created the ``User`` class by overloading the ``UserMixin`` class. The ``UserMixin`` class
implements some of the default methods, and hence is a convenient starting point. The ``dict`` ``user_database``
is a proxy for all the database code one would need. I am abstracting this away as a ``dict`` for simplicity.
The `get` class method returns the user data from `user_database`.


For the ``LoginManager`` to handle authentication, we have to provide a method for it to load user.
Here I use the generic ``@login_manager.request_loader`` decorator to decorate the ``load_user`` function.
The expected behavior of a ``request_loader`` is to return a ``User`` instance if the provided credentials are
valid, and return `None` otherwise.

.. code:: python

  @login_manager.request_loader
  def load_user(request):
      token = request.headers.get('Authorization')
      if token is None:
          token = request.args.get('token')
          
      if token is not None:
          username,password = token.split(":") # naive token
          user_entry = User.get(username)
          if (user_entry is not None):
              user = User(user_entry[0],user_entry[1])
              if (user.password == password):
                  return user
      return None 

The ``load_user`` looks for a token in ``Authorization`` header, or the ``request`` arguments. If a token
is provided, then I return an instance of ``User`` if the token is valid, and return ``None`` otherwise.
Here I assume that a valid token would be of the form ``<username>:<password>``. This is a naive token,
and should not be used in practice. Using serializers from ``itsdangerous`` package can come handy. We
will touch upon these issues in another post.

Once this setup is done, in order to require authentication for a route, use the ``@login_required``
decorator.

Run the above script, and if you visit the LocalHostUnAuthenticated_ route without 
a token you will get a ``401 Unauthorized`` message. If you pass a token to 
LocalHostAuthenticated_, then you will be allowed access to the protected page.


.. _LocalHostUnAuthenticated: http://localhost:5000/protected/
.. _LocalHostAuthenticated: http://localhost:5000/protected/?token=JohnDoe:John


Conclusion
----------

This article explained how to write token based authentication using ``Flask-Login`` extension. The focus
of this article was explaining the basic workings of ``flask-login`` without having to setup database or
even the token generation. Once the basic plumbing is setup, one can extend this example in two ways: 

- `Securing Authentication Tokens <{filename}securing-authentication-tokens.rst>`_
- have a database to store and retrive user credentials.






