from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name = "index"),
   path("display/", views.display, name = "display"),
   path("booking/", views.booking, name = "booking"),
   path("offers/", views.offers, name = "offers"),
   #path("<str:name>", views.greet, name = "greet"),
]