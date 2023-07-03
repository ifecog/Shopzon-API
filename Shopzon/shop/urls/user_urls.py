from django.urls import path
from shop.views import user_views as views

urlpatterns = [
    path('', views.get_users, name='users'),
    path('register/', views.register_user, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('profile/', views.get_user_profile, name='user-profile'),
    path('profile/update/', views.update_profile, name='update-profile'),
    path('<user_id>/', views.get_user_by_id, name='user'),
    path('update/<user_id>/', views.update_user_by_id, name='update-user'),
    path('delete/<user_id>/', views.delete_user_by_id, name='delete-user'),
]
