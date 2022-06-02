from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name="detail_order"),
    path('', views.ListOrder.as_view(), name="list_order"),
]
