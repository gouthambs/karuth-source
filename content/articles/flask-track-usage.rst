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
be released as part of version 1.0.0. 

Here is a quick-start version on using SQLStorage with Flask-Track-Usage:

.. code:: python

    # mainapp.py
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
    
    # Here app is the Flask app created in mainapp.py 
    app.config['TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS'] = 'include'

    # Make an instance of the extension
    t = TrackUsage(app, SQLStorage(conn_str="sqlite:///D:\\usage_tracking.db"))

    # exclude just the a_blueprint out
    from my_blueprints import a_blueprint
    t.exclude_blueprint(a_blueprint)

What we have done here is to include all views, except for the ones in the blueprint ``a_blueprint``.
You can instead exclude all by default, and include just the specific ones as shown below.

.. code:: python

    # Here app is the Flask app created in mainapp.py 
    app.config['TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS'] = 'exclude'
    
    # Make an instance of the extension
    t = TrackUsage(app, SQLStorage(conn_str="sqlite:///D:\\usage_tracking.db"))
    
    from my_blueprints import a_blueprint
    t.include_blueprint(a_blueprint)

Once you have setup the extension to track usage, you can even use the ``_get_usage`` method
part of the ``Storage`` object to view the usage hits. This method returns a list of JSON
dict and has the following schema::

    [
        {
                'url': str,
                'user_agent': {
                    'browser': str,
                    'language': str,
                    'platform': str,
                    'version': str,
                },
                'blueprint': str,
                'view_args': dict or None
                'status': int,
                'remote_addr': str,
                'authorization': bool,
                'ip_info': str or None,
                'path': str,
                'speed': float,
                'date': datetime,
        },
        {
            ....
        }
    ]

    

    
	