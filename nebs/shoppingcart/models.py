from __future__ import unicode_literals
from django.db import models
from main.models import Item

# Create your models here.

class client (models.Model):
    FirstName = models.CharField(max_length=120)
    LastName = models.CharField(max_length=120)
    Number = models.IntegerField()
    Address = models.CharField(max_length=500)

    def __str__(self):
        return self.FirstName + ' ' + self.LastName
        
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    OrderNumber = models.CharField(max_length = 2000,null=True,blank=True)
    is_ordered = models.BooleanField(default=False)
    subtotal = models.FloatField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"
    def cal_subtotal(self):
        return self.quantity*self.item.price

class Order (models.Model):
    STATUS = (('Pending', 'Pending'),
              ('Canceled', 'Canceled'),
              ('Sold', 'Sold')
    )
    client = models.ForeignKey(client, on_delete=models.CASCADE, null=True)    
    is_ordered = models.BooleanField(default=False)
    products = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    OrderNumber = models.CharField(max_length = 2000,null=True,blank=True)
    STATUS = models.CharField(max_length=50, default='Pending', choices=STATUS)
    def __str__(self):
        return '{0} - {1}'.format(self.OrderNumber, self.date_ordered)

    def get_cart_items(self):
        return self.products.all()
    
    def get_cart_total(self):
        return float(sum([item.cal_subtotal() for item in self.products.all()]))

class transaction (models.Model):
    date=models.DateTimeField(auto_now=True)
    revenues=models.FloatField(default=1,blank=True)
    Orders=models.ManyToManyField(Order)
    best_selling=[]
    def get_total_revenues(self):
        Total=0
        for element in self.Orders.all():
            if(element.date_ordered==date and STATUS=='Sold'):
                for qnt in element.products.all():
                   sum+=qnt.cal_subtotal
        return Total
class best_seller(models.Model):
    product=models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    date=models.DateTimeField(auto_now=True)