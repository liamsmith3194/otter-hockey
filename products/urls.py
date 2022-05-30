from django.urls import path
from . import views

urlpatterns = [
    path('sticks', views.stick_products, name='products'),
    path('bags', views.bag_products, name='products'),
    path('clothes', views.clothes_products, name='products'),
    path('accessories', views.accessories_products, name='products'),
]
