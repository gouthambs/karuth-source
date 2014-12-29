Flask App Directory Structure
#############################

:date: 2014-12-29
:tags: programming, flask, python
:slug: flask-app-directory-structure
:author: Gouthaman Balaraman
:description: Some notes on how to organize your flask app structure, and some thoughts on deployment.

This post is a summary of what I learnt perusing a lot of websites. My goal here is to:

- summarize the directory structure for a flask app
- setup SQLAlchemy with migrations 
- outline the setup for transition to production

Directory Structure
===================

I want to build a website based on the Flask framework for python. I recommend you organize you ``app`` as::

	~/AppHome
		|-- run.py
		|-- config.py
		|__ /myapp
			|-- __init__.py
			|__ /subapp1
				|-- __init__.py
				|-- models.py
				|-- views.py
				|-- viewmodel.py
			|__ /templates
				|-- base.html
				|-- index.html
				|__ /subapp1
					|-- subapp1_index.html
					|-- otherpage.html
			|__ /static
				|__ /js
				|__ /css
		|-- setup.py
		|-- MANIFEST.in
		|-- Requirements.txt
		|__ /env
		|
		|-- manage.py
		|__ /migrations
			|__ ...
		|__ /etl
			|__ ...
		|
		|-- fabfile.py
			
			
What I have shown above is the overall structure of a Flask application that will transition
over to production smoothly. Let me explain the structure briefly before we dive into any code.

- ``run.py`` is the actual python code that will import the app and execute
- ``config.py`` is the file for storing configurations for the app
- ``myapp`` is the folder containing the python code and its dependencies such as ``templates`` and ``static`` files
- ``myapp/__init__.py`` is typically where I create the Flask ``app`` instance and do all the configuration
- ``myapp/subapp1`` is a sub-package under the ``myapp`` packages. I recommend using sub-packages to organize
  your web application with the help of ``Blueprints``. 
  
	- ``myapp/subapp1/__init__.py`` is the place to create the ``Blueprint`` definition and other initializations 
	  corresponding to your sub-package.
	- ``myapp/subapp1/models.py`` is the place to define the SQLAlchemy models.
	- ``myapp/subapp1/views.py`` is the place to define the routes that the submodule will provide
	- ``myapp/subapp1/viewmodel.py`` is the bridge between model and view. Use this file to create functions 
	  to wrap your database queries using models defined in ``models.py that ``views.py`` can call. 
	  In the future, should you want to add caching support, you can directly add here and have the benefit of 
	  caching.
	  
  
		
		
				





