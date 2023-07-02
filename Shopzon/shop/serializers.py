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
    category = serializers.SerializerMethodField(read_only=True)
    brand = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_category(self, obj):
        category = obj.category_set.all()
        serializer = CategorySerializer(category, many=False)
        return serializer.data
    
    def get_brand(self, obj):
        brand = obj.brand_set.all()
        serializer = CategorySerializer(brand, many=False)
        return serializer.data
    
    