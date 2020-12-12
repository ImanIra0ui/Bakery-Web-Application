from django.urls import path
from . import views

app_name = "shoppingcart"

urlpatterns = [
   path("cart/", views.index, name = "index"),
]