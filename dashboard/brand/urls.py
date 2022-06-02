from django.urls import path
from . import views
from dashboard.decorators import permession


app_name='brand_dashboard'

urlpatterns = [
    path('create/', permession(views.CreateBrand.as_view()), name = 'create_brand'),
    path('update/<int:pk>/', permession(views.UpdateView.as_view()), name = 'update_brand'),
    path('list/', permession(views.ListBrand.as_view()), name = 'list_brand'),
    path('delete/<int:pk>', permession(views.delete_brand), name='delete_brand'),
    
]