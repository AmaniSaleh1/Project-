from django.urls import path, re_path
from apps.jewmodule import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('jewelry', views.jewelry, name = "jewelry"),
    path('jewelry/<int:bId>', views.jewelry, name="jewelry"),
    path('addjewelry', views.addjewelry, name='addjewelry'),
    path('updatejewelry/<int:bId>', views.updatejewelry, name="updatejewelry"),
    path('filterjewelry', views.filterjewelry, name="filterjewelry")
]
