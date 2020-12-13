from __future__ import unicode_literals
from django.db import models
from main.models import Item

# Create your models here.

class client (models.Model):
    FirstName = models.CharField(max_length=120)
    LastName = models.CharField(max_length=120)
    Number = models.IntegerField()

    def __str__(self):
        return self.FirstName + ' ' + self.LastName


class order (models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE, null=True)    
    is_ordered = models.BooleanField(default=False)
    products = models.ManyToManyField(Item)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} - {1}'.format(self.client, self.date_ordered)

    def get_cart_items(self):
        return self.products.all()
    
    def get_cart_total(self):
        return sum([item.price for item in self.products.all()])

