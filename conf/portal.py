# -*- coding:utf-8 -*-

# -- app config --
DEBUG = False

# -- db config --
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "root"
DB_PASS = ""
DB_NAME = "falcon_portal"

# -- cookie config --
SECRET_KEY = "4e.5tyg8-u9ioj"
SESSION_COOKIE_NAME = "falcon-portal"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30

UIC_ADDRESS = {
    'internal': 'http://127.0.0.1:1234',
    'external': 'http://127.0.0.1:1234',
}

UIC_TOKEN = ''

MAINTAINERS = ['root']
CONTACT = 'minimum@cepave.com'

COMMUNITY = True

try:
    from frame.local_config import *
except Exception, e:
    print "[warning] %s" % e

