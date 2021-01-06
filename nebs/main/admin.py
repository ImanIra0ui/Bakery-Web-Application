from django.contrib import admin
from .models import *


 

@admin.register(Item) 
class Revenue(admin.ModelAdmin):
    list_display = ( "name", "category","sold_qty")
