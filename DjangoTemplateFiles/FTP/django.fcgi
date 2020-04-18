#!/usr/www/spag/django/Spagistan/bin/python
import sys, os

# # Add a custom Python path.
# sys.path.insert(0, "/usr/www/spag/django/django-projects")
sys.path.insert(0, "/usr/www/spag/django/Spagistan")

# # Switch to the directory of your project. (Optional.)
# os.chdir("/usr/www/spag/django/django-projects/sample_project")
os.chdir("/usr/www/spag/django/Spagistan")

# # Set the DJANGO_SETTINGS_MODULE environment variable.
# os.environ['DJANGO_SETTINGS_MODULE'] = "sample_project.settings"
os.environ['DJANGO_SETTINGS_MODULE'] = "Spagistan.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
