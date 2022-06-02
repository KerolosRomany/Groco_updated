from django.urls import path
from .views import *

app_name = "checkout"

urlpatterns = [
    path('', checkout_view, name="checkout_index"),
    path('create/address/', create_address, name="checkout_create_address"),
    path('edit/address/', edit_address, name="checkout_edit_address"),
    path('edit/address/', create_order, name="create_order")

]
