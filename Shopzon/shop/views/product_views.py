from django.shortcuts import render, get_object_or_404

from shop.models import Brand, Category, Product
from shop.serializers import ProductSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def get_products(request):
    category_id = request.query_params.get('category')
    brand_id = request.query_params.get('brand')
    
    products = Product.objects.all()
    
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    if brand_id:
        brand = get_object_or_404(Brand, id=brand_id)
        products = products.filter(brand=brand)

    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_toprated_products(request):
    products = Product.objects.filter(rating__gte=4).order_by('-rating')
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)
