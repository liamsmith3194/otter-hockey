from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all'),
    path('sticks', views.stick_products, name='sticks'),
    path('bags', views.bag_products, name='bags'),
    path('clothes', views.clothes_products, name='clothes'),
    path('accessories', views.accessories_products, name='accessories'),
    path('<product_id>', views.product_detail, name='product_detail'),

]
