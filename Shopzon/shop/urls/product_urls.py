from django.urls import path
from shop.views import product_views as views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('toprated_products/', views.get_toprated_products, name='toprated-products'),
    path('<product_id>/', views.get_product_details, name='product-details'),
    path('<product_id>/reviews/', views.create_product_review, name='product-reviews'),
]
