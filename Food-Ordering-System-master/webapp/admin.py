from django.contrib import admin
from .models import Customer, Restaurant, Item, Menu, Order, orderItem, User, Product, OrderHistory

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(orderItem)
admin.site.register(Product)
admin.site.register(OrderHistory)
