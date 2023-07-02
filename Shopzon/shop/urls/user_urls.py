from django.urls import path
from shop.views import user_views as views

urlpatterns = [
    path('', views.get_users, name='users'),
    path('register/', views.register_user, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('profile/', views.get_user_profile, name='user-profile'),
]
