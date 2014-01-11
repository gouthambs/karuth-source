#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gouthaman Balaraman'
SITENAME = u'Karuth'
#SITESUBTITLE	= u"Truth in Numbers"
SITEURL = 'http://www.karuth.com'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT ='%B %d, %Y'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
TWITTER_HANDLE = 'quantspeak'
#SOCIAL = (('Twitter','https://twitter.com/'+TWITTER_HANDLE),)
            #(('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

READERS = {'html': None}
DISQUS_SITENAME = "karuth"
GOOGLE_ANALYTICS = 'UA-46714334-1'
THEME = "svbhack-theme"
DISPLAY_PAGES_ON_MENU = True
PATH = "content"
