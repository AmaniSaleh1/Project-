<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f805db6a1790a2fd31e46ec097a587081675bc65
from django.urls import path, re_path
from apps.jewmodule.views import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jewelry', views.jewelry),
    path('jewelry/<int: jew id>', views.jewelry),
]
<<<<<<< HEAD

from django.urls import path
from apps.jewmodule.views import index

urlpatterns = [
    path('', index, name='index'),
]
=======
=======
from django.urls import path
from apps.jewmodule.views import index

urlpatterns = [
    path('', index, name='index'),
]
>>>>>>> 65a4a5d96c0f434d53e3290270e7c145a1ddb7f3
>>>>>>> f805db6a1790a2fd31e46ec097a587081675bc65
