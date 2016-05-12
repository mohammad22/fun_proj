"""
WSGI config for fun_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fun_proj.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fun_proj.settings")

application = Cling(MediaCling(get_wsgi_application()))



