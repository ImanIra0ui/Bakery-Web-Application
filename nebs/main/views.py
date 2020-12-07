from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def display(request):
    #Get all Items from DB
    #Figure out how to filter it based on category
    all_items = Item.objects.all() 
    return render(request, "main/display.html", {'Items' : all_items})

def booking(request):
    return HttpResponse("Book Page")

def offers(request):
    return HttpResponse("Offers Page")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")

