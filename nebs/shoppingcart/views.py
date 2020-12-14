from django.shortcuts import render
from django import forms
from main.models import Item
# Create your views here.

Ids = []

#class NewItemForm (forms.Form):
#    Item_id = forms.IntegerField(label="id")

def index(request):
    if request.method=="POST":
        Item_id = request.POST['product']
        obj = Item.objects.get(id=Item_id)
        Ids.append(obj)
        quant = 1
        total = 0

        for i in range (len(Ids)):
            total = total+Ids[i].price

        return render(request, "main/shoppingcart.html", {
            "Item_id": Ids,
            "quant" : quant,
            "total": total
        })

    #if request.method == "POST":
      #  form = NewItemForm(request.POST)

       # if form.is_valid():
        #    It_id = form.cleaned_data["id"]
         #   Ids.append(It_id)
          #  return render(request, "main/shoppingcart.html", {
           #     "Item_i": It_id
            #})
        #else:
         #   return render(request, "main/display.html", {
          #      "form": NewItemForm()
           # })
    #else:
    else:
        return render(request, "main/shoppingcart.html", {
            "Item_id" : Ids
        })

    