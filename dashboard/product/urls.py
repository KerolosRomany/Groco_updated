from django.urls import path
from . import views
from dashboard.decorators import permession

app_name = 'product_dashboard'

urlpatterns = [
    path('create/', permession(views.CreateProduct.as_view()), name='product_create'),
    path('update/<int:pk>/', permession(views.UpdateProduct.as_view()), name='product_update'),
    path('list/', permession(views.ListProduct.as_view()), name='product_list'),
    path('<int:pk>/list/images/', permession(views.ProductImageList.as_view()), name='product_image_list'),
    path('<int:pk>/create/image/', permession(views.create_image), name='create_image'),
    path('delete/image/<int:pk>', permession(views.delete_image), name='delete_image'),

    path('delete/<int:pk>', permession(views.delete_product), name='delete_product'),
    
]
