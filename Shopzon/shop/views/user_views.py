from django.shortcuts import render, get_object_or_404
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
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)
    
    data = request.data
    # update user fields
    user.first_name=data['first_name'],
    user.last_name=data['last_name'],
    user.username=data['email'], 
    user.email=data['email'], 
    if data['password'] != '':
        user.password=make_password(data['password'])
    
    user.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_by_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    data = request.data
    
    # update fields
    user.first_name=data['first_name'],
    user.last_name=data['last_name'],
    user.email=data['email'],
    user.is_staff=data['isAdmin']

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_user_by_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    data = request.data
    serializer = UserSerializer(user, many=False)
    
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user_by_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return Response('User Deleted!')



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
