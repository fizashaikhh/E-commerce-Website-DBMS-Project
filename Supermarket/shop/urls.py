from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="shophome"),
path("products/<int:id>",views.productView, name="ProductView"),
path("checkout",views.checkout, name="checkout")
]