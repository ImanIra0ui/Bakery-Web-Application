from django.shortcuts import render, get_object_or_404
from django import forms
from main.models import Item
from shoppingcart.models import OrderItem, Order, client
from datetime import datetime

# Create your views here.

def confirm (request):
    if not request.session.session_key:
        request.session.save()
    if not request.session.session_key:
        request.session.save()

    order_qs = Order.objects.filter(session=request.session.session_key+"1", is_ordered=False)

    if order_qs.exists():
        order = order_qs[0]   
        if request.method=="POST":
            FirstName = request.POST['fname']
            LastName = request.POST['lname']
            Number = request.POST['number']
            Address = request.POST['address']
            Total = request.POST.get('ttl', False)
        
            client2 = client.objects.create(FirstName = FirstName, LastName = LastName, Number = Number, Address=Address)
            order.client = client2
            order.is_ordered = True
            order.save()

            x=0
            
            for i in order.products.all():
                x += (i.item.price)*(i.quantity)

            if(Address == " "):
                order.delivery = False
                order.total = x
            else:
                x = float(Total) + 15.0 
                order.delivery = True
                order.total = x
            
            order.save()

            now = datetime.now()
            now1 = now.strftime("%m/%d/%Y, %H:%M:%S")

            order.session = now1 + request.session.session_key+"1"
            order.save()

            for i in order.products.all():
                i. session = request.session.session_key+ "1" + now1,
                i.is_ordered = True
                i.save()
            
            
     
        return render(request, "main/shoppingcart.html", {
                    "Item_id": [],
                    "total": 0
                })

        

    else:
        return render(request, "main/shoppingcart.html", {
                    "Item_id": [],
                    "total": 0
                })



def index(request):
    total = 0

    if not request.session.session_key:
        request.session.save()

    order_qs = Order.objects.filter(session=request.session.session_key+"1", is_ordered=False)

    if order_qs.exists():
        order = order_qs[0]

    else:
        order = Order.objects.create(session=request.session.session_key+"1")

    if request.method=="POST":
        Item_id = request.POST['product']
        item = Item.objects.get(id=Item_id)
        #order_item = Item.objects.get(id=Item_id)
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            session = request.session.session_key+"1",
            is_ordered= False
        )
        order_qs = Order.objects.filter(session=request.session.session_key+"1", is_ordered=False)
        
        if order_qs.exists():
            order = order_qs[0]
            
            #check if orderitem is in order
            if order.products.filter(item__id=item.id).exists():
                order_item.quantity += 1
                order_item.save()
            else:
                order.products.add(order_item)
                order.save()

        else:
            order = Order.objects.create(session=request.session.session_key+"1")
            order.products.add(order_item__id)
            order.save()

        for i in order.products.all():
            total += (i.item.price)*(i.quantity)

        order_item.subtotal = order_item.item.price*order_item.quantity
        order_item.save()

        return render(request, "main/shoppingcart.html", {
            "Item_id": order.products.all(),
            "total": total
        })

    else:

        order_qs = Order.objects.filter(session=request.session.session_key+"1", is_ordered=False)


        if order_qs.exists():
            order = order_qs[0]

            total = 0

            for i in order.products.all():
                total += (i.item.price)*(i.quantity)

            return render(request, "main/shoppingcart.html", {
                    "Item_id": order.products.all(),
                    "total": total
                })
        else:
            return render(request, "main/shoppingcart.html", {
                    "Item_id": [],
                    "total": total
                })

    