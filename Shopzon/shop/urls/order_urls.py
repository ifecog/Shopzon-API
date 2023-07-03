from django.urls import path
from shop.views import order_views as views

urlpatterns = [
    path('', views.get_orders, name='orders'),
    path('add/', views.add_order_items, name='add-order'),
    path('myorders/', views.get_my_orders, name='my-orders'),
    path('<order_id>/', views.get_order_by_id, name='get-order'),
    path('<order_id>/payment/', views.update_order_to_paid, name='order-payment'),
    path('<order_id>/delivery/', views.update_order_to_delivered, name='order-delivery'),
]