from django.contrib import admin

# Register your models here.

from .models import *
import datetime



admin.site.register(OrderItem)
def cancel(modeladmin, request, queryset):
    queryset.update(STATUS='Canceled')

def make_sold(modeladmin, request, queryset):
    queryset.update(STATUS='Sold')
    print(queryset)
    now=datetime.datetime.now()
    tmp=0
    for t in transaction.objects.all():
        if t.date.day==now.day and t.date.month==now.month and t.date.year==now.year:
            for element in queryset:
                t.Orders.add(element)
                t.revenues+=element.get_cart_total()
                t.save()
                tmp=1
                break
    if tmp==0:
        f=transaction(date=now,revenues=0.0)
        f.save()
        for element in queryset:
               f.Orders.add(element)
               f.revenues=f.revenues+element.get_cart_total()  
               f.save()
    for element in queryset:
          for j in OrderItem.objects.all():
               llist =Order.objects.filter(products=j)
               for c in llist:
                    if c==element:
                         j.item.sold_qty=j.item.sold_qty+j.quantity
                         j.item.available_qty= j.item.available_qty-j.quantity
                         j.item.save()
make_sold.short_description = "SELL"

#def date_iter(year, month):
    #for i in range(1, calendar.monthlen(year, month) + 1):
     #   yield date(year, month, i)

#def generate_revenues(modeladmin, request,)
 #   now=datetime.datetime.now()
    #for d in date_iter(now.year(), now.month()):
      #  tmp=0
       # for t in transaction.objects.all():
        #    if t.date==d:
         #       tmp=1
          #      break
        #if tmp==0:
         #   f=transaction(date=d,revenues=0.0,orders=[])
        #for element in Order.objects.all():
         # if (element.date_ordered==d and element.status='Selled'):
          #     f.orders.add(element)
           #    f.revenues+=element.get_cart_total()
        #f.save()              

@admin.register(Order) 
class OrderAdmin(admin.ModelAdmin):
    list_display = ("client", "date_ordered", "STATUS","is_ordered")
    list_filter = ("date_ordered",)
    actions = [make_sold,cancel]
    
@admin.register(transaction) 
class Revenue(admin.ModelAdmin):
    list_display = ( "date", "revenues")
    list_filter = ("date",)
    #actions = [generate_revenues]
@admin.register(best_seller) 
class Revenue(admin.ModelAdmin):
    list_display = ( "product","date")
    list_filter = ("date",)
@admin.register(client) 
class Revenue(admin.ModelAdmin):
    list_display = ( "FirstName","LastName","Number")