"""
WSGI config for cookbook project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from web.django import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cookbook.settings")

application = get_wsgi_application()
