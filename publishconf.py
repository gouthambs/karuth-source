#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gouthaman Balaraman'
SITENAME = u'Gouthaman Balaraman'
SITEURL = 'http://gouthamanbalaraman.com'
LOCAL_BOOTSTRAP  = True
#SITEURL = '/'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'


TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT ='%B %d, %Y'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'
STATIC_PATHS = [
    'robots.txt', 'extra', 'images'
    ]

PLUGIN_PATHS = ['./pelican-plugins/']
PLUGINS = ['render_math', 'related_posts']
RELATED_POSTS_MAX = 5

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
TWITTER_HANDLE = 'gsbala'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
READERS = {'html': None}
DISQUS_SITENAME = "gouthamanbalaramancom"
GOOGLE_ANALYTICS = 'UA-46714334-1'
THEME = "simple-bootstrap"
DISPLAY_PAGES_ON_MENU = True
PATH = "content"
