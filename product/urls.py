from django.urls import path
from .views import detail_product, ListOfProduct,add_product_to_checkout
from product import views

app_name = "product"

urlpatterns = [
    path('', views.all_products, name="all_products"),
    path('<str:slug>/', detail_product, name='detail_product'),
    path('add/<int:pk>/', add_product_to_checkout, name='add_product_to_checkout'),
]
