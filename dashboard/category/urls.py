from django.urls import path
from . import views
from dashboard.decorators import permession
app_name='category_dashboard'

urlpatterns=[

    path('create/',permession(views.CreateCategory.as_view()), name="category_create"),
    path('list/', permession(views.CategoryList.as_view()), name="category_list"),
    path('update/<int:pk>/', permession(views.UpdateCategory.as_view()), name="category_update"),
    path('<int:pk>/', permession(views.category_detail), name="category_detail"),
    path('create/<int:pk>/', permession(views.CreateSubCategory.as_view()), name="sub_category_create"),
    path('delete/<int:pk>', permession(views.delete_category), name='delete_category'),
    
]