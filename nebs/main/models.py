from django.db import models
from enum import Enum

class ItemCategory(Enum):
    CAKE = 'Cake',
    BREAD = 'Bread',
    PASTRY = 'Pastry',
    COOKIES = 'Cookies',
    MOROCCAN = 'Moroccan'

    @classmethod
    def ch(self):
        r = []
        for i in ItemCategory:
            r.append((i.name, i.value))




# Create your models here.

class Item(models.Model):
    picture = models.ImageField(upload_to = 'main/static/main/imgs/item-pictures')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length = 250)
    category = models.CharField(
        max_length= 30,
        choices = ItemCategory.ch()
    )


