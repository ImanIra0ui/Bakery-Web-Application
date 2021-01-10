"""
WSGI config for nebs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application


import os
#from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nebs.settings')

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)

