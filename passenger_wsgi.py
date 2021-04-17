# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/g/gldmeister/zandau.kz/public_html/instaway')
sys.path.insert(1, '/home/g/gldmeister/zandau.kz/public_html/venv_django/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'instaway.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()