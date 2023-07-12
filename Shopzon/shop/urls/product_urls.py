from django.urls import path
from shop.views import product_views as views

urlpatterns = [
    path('', views.get_products, name='get-products'),
    path('create/', views.create_product, name='create-product'),
    path('image-upload/', views.upload_image, name='image-upload'),
    path('toprated_products/', views.get_toprated_products, name='toprated-products'),
    path('<int:product_id>/reviews/', views.create_product_review, name='product-reviews'),
    path('<int:product_id>/', views.get_product_details, name='product-details'),
    path('<int:product_id>/update/', views.update_product, name='update-product'),
    path('<int:product_id>/delete/', views.delete_product, name='delete-product'),
]
