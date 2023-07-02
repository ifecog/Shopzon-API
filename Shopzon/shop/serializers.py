from django.contrib.auth.models import User
from .models import Brand, Category, Product

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = '__all__'
        

class BrandSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Brand
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)    
    class Meta:
        model = Product
        fields = '__all__'
            
    