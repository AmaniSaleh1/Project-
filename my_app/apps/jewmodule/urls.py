from django.urls import path
from apps.jewmodule.views import index

urlpatterns = [
    path('', index, name='index'),
]
