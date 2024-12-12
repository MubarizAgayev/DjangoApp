from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('reserve/', views.reserve_room, name='reserve_room'),
    path('offers/', views.special_offers, name='special_offers'),
]
