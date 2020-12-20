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


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    session = models.CharField(max_length = 2000)
    is_ordered = models.BooleanField(default=False)
    subtotal = models.FloatField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

class Order (models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE, null=True)    
    is_ordered = models.BooleanField(default=False)
    products = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    session = models.CharField(max_length = 2000)

    def __str__(self):
        return '{0} - {1}'.format(self.session, self.date_ordered)

    def get_cart_items(self):
        return self.products.all()
    
    def get_cart_total(self):
        return sum([item.price for item in self.products.all()])

