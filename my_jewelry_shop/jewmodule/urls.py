from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jewelry/', views.jewelry_list, name='jewelry_list'),
    path('jewelry/<int:pk>/', views.jewelry_detail, name='jewelry_detail'),
    path('jewelry/add/', views.add_jewelry, name='add_jewelry'),
    path('jewelry/<int:pk>/update/', views.update_jewelry, name='update_jewelry'),
    path('jewelry/<int:pk>/delete/', views.delete_jewelry, name='delete_jewelry'),
    path('filter_jewelry/', views.filter_jewelry, name='filter_jewelry'),  # Add this line
]
