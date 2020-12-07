from django.db import models


# Create your models here.

#How a product will look like
class Item(models.Model):
    CATEGORY = (
        ('Cake', 'Cake'),
        ('Bread', 'Bread'),
        ('Pastry', 'Pastry'),
        ('Cookies', 'Cookies'),
        ('Moroccan', 'Moroccan')
    )
    picture = models.ImageField(upload_to = 'main/static/item-pictures')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length = 250)
    category = models.CharField(
        max_length= 30,
        choices = CATEGORY
    )
    sold_qty = models.IntegerField()
    available_qty = models.IntegerField()  


