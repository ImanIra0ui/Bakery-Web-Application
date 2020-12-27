from django.http import HttpResponse
from django.shortcuts import render
from .models import Item, Booking
from django.contrib import messages
from django.core import serializers
from json import dumps 
import json



# Create your views here.
def index(request):
    return render(request, "main/index.html")

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

