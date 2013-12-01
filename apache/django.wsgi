import os
import sys

apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)

sys.path.append('/home/ec2-user/django-personal-website')
sys.path.append('/home/ec2-user/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'home.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()