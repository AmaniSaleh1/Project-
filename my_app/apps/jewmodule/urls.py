from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jewelry/', views.jewelry_list, name='jewelry_list'),
    path('jewelry/<int:bId>/', views.jewelry_detail, name='jewelry_detail'),
    path('addjewelry/', views.add_jewelry, name='add_jewelry'),
    path('updatejewelry/<int:bId>/', views.update_jewelry, name='update_jewelry'),
    path('filterjewelry/', views.filter_jewelry, name='filter_jewelry'),
]
