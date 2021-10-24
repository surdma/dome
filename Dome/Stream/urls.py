from django.urls import path, include
from .views import Home,class_room

urlpatterns = [
    path('', Home, name='index'),
    path('class/', class_room, name='class'),
    ]
