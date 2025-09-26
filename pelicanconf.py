AUTHOR = 'Amit Hazi'
SITENAME = 'Amit Hazi'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

#MENUITEMS = (('Pelican', 'https://getpelican.com/'),)

# Social widget
SOCIAL = (# ('email', 'A.Hazi@leeds.ac.uk'),
          ('arxiv', 'http://arxiv.org/a/hazi_a_1'), 
          ('orcid', 'https://orcid.org/0000-0001-7264-2211'),
          ('google-scholar', 'https://scholar.google.com/citations?user=DeEDVdkAAAAJ&hl=en'),
          ('github', 'https://github.com/amithazi'),)
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
PAGE_ORDER_BY = 'order'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# theme-related settings
THEME = 'theme-pelican-hyde'
#DISPLAY_HOME = False
FONT_ACADEMICONS = True

PROFILE_IMAGE = 'square-headshot.jpg'
