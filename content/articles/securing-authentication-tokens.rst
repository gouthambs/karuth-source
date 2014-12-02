Securing Authentication Tokens
##############################

:date: 2014-12-02
:tags: Programming, Python, Flask, Authentication
:slug: securing-authentication-tokens
:author: Gouthaman Balaraman
:description: This post will give a basic discussion on securing authentication tokens
 that can be used with Flask-Login.
:keywords: Flask, Python, Programming, Analytics, Authentication, Flask-Login, Flask Login, itsdangerous

The article `Minimal Flask Login Example <|filename|minimal_flask_login_example.rst>`_ provided an introduction to token 
based authentication using the Flask-Login extension for the Flask web framework. The focus of that article was to
highlight the crux of authentication logic. One glaring omission was that the token itself was nothing but
the username and password passed as clear text. This clearly will not work! 

The high level control flow involving token based authentication is as follows:

- client (browser) makes a *request* for the web token in exchange for authentication credential
- the authentication credentials are serialized to create a token, and server *responds* with this token
- every time the client needs to *request* a secured page, the client would provide the authentication token to the server
  part of the request
- the server deserializes the token, fetches the authentication credentials and validates the token
- if the token is valid, then the server responds with an access to the secured page; should the token be invalid, then
  the access to secured page is denied.
  
In the `Minimal Flask Login Example <|filename|minimal_flask_login_example.rst>`_, we skipped the serialization part
for simplicity. A more rigorous way of doing this would be to use ``JSONWebSignatureSerializer`` in the 
``itsdangerous`` package to serialize the authentication credentials.

.. code:: python
  
  from itsdangerous import JSONWebSignatureSerializer
  s = JSONWebSignatureSerializer('secret-key')
  token = s.dumps({'username': JaneDoe, 'password' : 'secret'})
  
The ``token`` in the above code can be used to pass from the server side. Validating a token is 
simple as well.

.. code:: python

  from itsdangerous import JSONWebSignatureSerializer
  s = JSONWebSignatureSerializer('secret-key')
  credential = s.loads(token)

The above code will get the ``credential`` corresponding to the user which can then be checked against what is 
stored in the database.


  
  

  
  
