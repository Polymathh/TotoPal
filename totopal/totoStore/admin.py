from django.contrib import admin
from .models import Product, ProductMedia , CartItem, Order
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductMedia)
admin.site.register(CartItem)
admin.site.register(Order)