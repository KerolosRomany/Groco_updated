from django.urls import path
from .views import detail_product, add_product_to_checkout
from product import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "product"

urlpatterns = [
    path('', views.all_products, name="all_products"),
    path('<str:slug>/', detail_product, name='detail_product'),
    path('add/<int:pk>/', add_product_to_checkout, name='add_product_to_checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
