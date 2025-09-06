from django.contrib import admin
from .models import special_products, comment, address, CartItem, Order, OrderItem
# Register your models here.
admin.site.register(special_products)
admin.site.register(comment)
admin.site.register(address)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
