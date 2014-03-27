Usage Tracking for Flask Apps
#############################

:date: 2014-3-26
:tags: Programming, Python
:slug: flask-track-usage
:author: Gouthaman Balaraman
:description: Flask Track Usage is a very light weight Flask extension to track usage traffic for Flask apps.
 This post will give you a brief introduction to the usage and merits.
:keywords: Flask, Python, Programming, Analytics

Recently I had a requirement to add light weight tracking for a Flask app. Tools like Google analytics was not
an option because, I wanted raw number and data handy rather than just figures, this was a website page in the intranet, and  
I also wanted to easily track all the REST apis. That is when I stumbled upon `Steve Milner's <http://www.stevemilner.org/>`_ 
`Flask-Track-Usage` package.

The API and usage is incredibly simple, and as of version 0.0.7 supported Mongo DB storage. Since Mongo was not an
option for me, I added SQLAlchemy based storage, thus opening doors for a wide array of databases. These additions will
be released as part of version 0.0.8. 

Here is a quick-start version on using SQLStorage with Flask-Track-Usage:

.. code:: python

    # Create the Flask 'app'
    from flask import Flask
    app = Flask(__name__)

    # Set the configuration items manually for the example
    app.config['TRACK_USAGE_USE_FREEGEOIP'] = False
    app.config['TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS'] = 'include'

    # We will just print out the data for the example
    from flask.ext.track_usage import TrackUsage
    from flask.ext.track_usage.storage.sql import SQLStorage

    # Make an instance of the extension
    t = TrackUsage(app, SQLStorage(conn_str="sqlite:///D:\\usage_tracking.db"))

    # Make an instance of the extension
    t = TrackUsage(app, storage)

    # Include the view in the metrics
    @t.include
    @app.route('/')
    def index():
        return "Hello"

    # Run the application!
    app.run(debug=True)

In the code above, the `SQLStorage` object is created with a `conn_str` argument which can be 
any of the `engine configurations <http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html>`_ 
supported by SQLAlchemy itself. 

You can use Flask-Track-Usage with blueprints as well. This is how you include blueprints views:

.. code:: python
    
    # ...
    app.config['TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS'] = 'include'

    # Make an instance of the extension
    t = TrackUsage(app, SQLStorage(conn_str="sqlite:///D:\\usage_tracking.db"))

    from my_blueprints import a_blueprint

This is how you exclude blueprints

.. code:: python

    # ...
    app.config['TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS'] = 'exclude'
    from my_blueprints import b_blueprint
    
    # Now ALL of b_blueprints will be in the exclude list
    t.exclude_blueprint(b_blueprint)

You can even use the `get_usage` method in the `Storage` object to include
usage statistics part of your web application.


    
    
	