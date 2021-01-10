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
    #quantity = models.IntegerField()

    def __str__(self):
        return self.category+ ': ' + self.name


#How a booking will look like
class Booking(models.Model):
    #Add status
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    description = models.CharField(max_length = 250)
    def __str__(self):
        return self.name+ ': ' + self.day + " " + self.time



