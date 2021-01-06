from django.http import HttpResponse
from django.shortcuts import render
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
    return HttpResponse("Book Page")

def offers(request):
    return HttpResponse("Offers Page")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")


