from django.contrib import admin

# Register your models here.
# python manage.py makemigrations && python manage.py migrate

from .models import *

#registering Item 
admin.site.register(Item)
#registering Booking
admin.site.register(Booking)
