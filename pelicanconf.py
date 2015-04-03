#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gouthaman Balaraman'
SITENAME = u'Gouthaman Balaraman'
#SITEURL = '/'
LOCAL_BOOTSTRAP = True
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'


TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT ='%B %d, %Y'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'
STATIC_PATHS = [
    'robots.txt','extra','images'
    ]

#plugin parameters
PLUGIN_PATHS = ['./pelican-plugins/']
PLUGINS = ['related_posts', 'share_post']

RELATED_POSTS_MAX = 5


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
TWITTER_HANDLE = 'gsbala'
#SOCIAL = (('Twitter','https://twitter.com/'+TWITTER_HANDLE),)
            #(('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
#LOCAL_BOOTSTRAP = True

READERS = {'html': None}
THEME = "simple-bootstrap"
DISPLAY_PAGES_ON_MENU = True
PATH = "content"
