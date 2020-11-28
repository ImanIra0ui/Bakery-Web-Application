from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def booking(request):
    return HttpResponse("Book Page")

def offers(request):
    return HttpResponse("Offers Page")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")

