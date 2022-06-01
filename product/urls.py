from django.urls import path
from .views import ProductDetails, ListOfProduct
from product import views

app_name = "product"

urlpatterns = [
    path('', views.all_products, name="all_products"),
    path('<str:slug>/', ProductDetails.as_view(), name='detail_product'),
    path('category/<str:slug>/', ListOfProduct.as_view(), name='list_product'),
]
