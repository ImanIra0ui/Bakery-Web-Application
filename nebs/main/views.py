from django.http import HttpResponse
from django.shortcuts import render
from .models import Item, Booking
from django.contrib import messages
from django.core import serializers
from json import dumps 
import json



from .models import Item
from shoppingcart.models import best_seller
import datetime
# Create your views here.
def index(request):
    now=datetime.datetime.now()
    best_selling=[]
    for obj in best_seller.objects.all():
        if(now.month==obj.date.month and now.year==obj.date.year):
             best_selling.append(obj.product)
    if(not best_selling or now.day==1):
        best_selling=Item.objects.all().order_by('-sold_qty')[:8]
        for itm in best_selling:
            j=best_seller(product=itm , date=now)
            j.save()
    return render(request, "main/index.html",{'list':best_selling})
    

def display(request, cat):  
    #Get all Items from DB and Filter it based on category
    all_items = Item.objects.filter(category = cat)
    return render(request, "main/display.html", {'Items' : all_items})
  
def search(request):
    query = request.GET['query']
    all_items = Item.objects.filter(name__icontains = query)
    params = {'Items' : all_items}
    return render(request, "main/display.html", params)

def booking(request):
    if request.method == 'POST':
        name_value = request.POST['name']
        email_value = request.POST['email']
        phone_value = request.POST['phone']
        time_value = request.POST['time']
        day_value = request.POST['day']
        description_value = request.POST['description']
        if Booking.objects.filter(day = day_value, time = time_value).exists() == False:
            b = Booking.objects.create(name = name_value, email = email_value, phone = phone_value, day = day_value, time = time_value, description = description_value)
        else:
            messages.error(request,'The time slot selected is already taken')
    #Serializing Booking
    book = json.loads(serializers.serialize('json', Booking.objects.all(), fields=('day','time')))
    return render(request, "main/booking.html", {'data': json.dumps(book)})


def offers(request):
    return HttpResponse("Offers Page")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")


