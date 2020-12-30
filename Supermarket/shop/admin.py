from django.contrib import admin
from .models import Product, Category, Customer, Order, Supplier, OrderDetails
# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Product)
admin.site.register(Supplier)