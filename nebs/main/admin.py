from django.contrib import admin
from .models import *


 


#registering Booking
admin.site.register(Booking)
@admin.register(Item) 
class Revenue(admin.ModelAdmin):
    list_display = ( "name", "category","sold_qty")
