from django.urls import path
from shop.views import user_views as views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
]
