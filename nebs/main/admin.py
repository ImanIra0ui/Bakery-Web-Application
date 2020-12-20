from django.contrib import admin

# Register your models here.
# python manage.py makemigrations && python manage.py migrate

from .models import *

#registering Item 
admin.site.register(Item)
admin.site.register(Booking)
