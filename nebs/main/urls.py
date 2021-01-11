from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
   path("", views.index, name = "index"),
   path("display/<str:cat>/", views.display, name = "display"),
   path("search/", views.search, name = "search"),
   path("booking/", views.booking, name = "booking"),
   path("offers/", views.offers, name = "offers"),
   #path("<str:name>", views.greet, name = "greet"),
]