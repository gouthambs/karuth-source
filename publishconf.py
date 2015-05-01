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
PLUGINS = ['related_posts', 'share_post', 'liquid_tags.notebook']
RELATED_POSTS_MAX = 5

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
# TRANSLATION_FEED_ATOM = None

# Social widget
TWITTER_HANDLE = 'gsbalaraman'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
READERS = {'html': None}
DISQUS_SITENAME = "gouthamanbalaramancom"
GOOGLE_ANALYTICS = 'UA-46714334-1'
THEME = "simple-bootstrap"
DISPLAY_PAGES_ON_MENU = True
PATH = "content"


# handle ipython notebooks
NOTEBOOK_DIR = "extra/notebooks"
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')