from django.contrib import admin

# Register your models here.

from .models import *

#registering Item 
admin.site.register(client)
admin.site.register(Order)
admin.site.register(OrderItem)