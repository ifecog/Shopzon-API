from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status

from shop.serializers import UserSerializer, MyTokenObtainPairSerializer, UserSerializerWithToken


@api_view(['POST'])
def register_user(request):
    data = request.data
    
    try:
        user = User.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with email already exists, please login!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
