from django.urls import path, re_path
from apps.jewmodule import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('jewelry', views.jewelry, name = "jewelry"),
    path('jewelry/<int:bId>', views.jewelry),
    path('filter_jewelry', views.filter_jewelry, name="filter_jewelry")
]