from django.urls import path
from shop.views import order_views as views

urlpatterns = [
    path('', views.get_orders, name='orders'),
    path('add/', views.add_order_items, name='add-order'),
    path('myorders/', views.get_my_orders, name='my-orders'),
]