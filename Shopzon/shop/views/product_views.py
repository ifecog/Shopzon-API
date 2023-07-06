from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from shop.models import Brand, Category, Product, Review
from shop.serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def get_products(request):
    category_id = request.query_params.get('category')
    brand_id = request.query_params.get('brand')
    
    query = request.query_params.get('keyword')
    if not query:
        query = ''    
        
    products = Product.objects.filter(name__icontains=query)
    
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    if brand_id:
        brand = get_object_or_404(Brand, id=brand_id)
        products = products.filter(brand=brand)
        
    page = request.query_params.get('page')
    paginator = Paginator(products, 8)
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    if not page:
        page = 1
    page=int(page)

    serializer = ProductSerializer(products, many=True)
    
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def get_toprated_products(request):
    products = Product.objects.filter(rating__gte=3).order_by('-rating')[0:5]
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def get_product_details(request, product_id):
    product = get_object_or_404(Product, _id=product_id)
    serializer = ProductSerializer(product, many=False)
    
    return Response(serializer.data)


@api_view(['POST'])
def upload_image(request):
    data = request.data
    
    product_id = data['product_id']
    product = get_object_or_404(Product, _id=product_id)    
    product.image = request.FILES.get('image')
    product.save()
    
    return Response('Image successfully uploaded!')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product_review(request, product_id):
    user = request.user
    product = get_object_or_404(Product, _id=product_id)
    data = request.data
    
    # 1. review already exists from user
    already_exists = product.review_set.filter(user=user).exists()
    
    if already_exists:
        message = {'detail': 'Product already reviewed by user'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    # 2. No rating or 0 rating
    elif data['rating'] == 0:
        message = {'detail': 'kindly select a rating'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    # create new review
    else:
        review = Review.objects.create(
            product=product,
            user=user,
            name=user.first_name,
            rating=data['rating'],
            comment=data['comment']
        )
        reviews = product.review_set.all()
        product.num_of_reviews = len(reviews)
        
        total = 0
        for i in reviews:
            total += i.rating
            
        product.rating = total/len(reviews)
        product.save()
        
        return Response('Review Added')
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_product(request):
    user = request.user
    category = Category.objects.create(
        name='Test Category',
        description='Test desctiption'
    )
    brand = Brand.objects.create(
        name='Test Brand',
        description='Test desctiption'
    )
    product = Product.objects.create(
        user=user,
        category=category,
        brand=brand,
        name='sample name',
        description='',
        price=0,
        count_in_stock=0
    )
    serializer = ProductSerializer(product, many=False)
    
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_product(request, product_id):
    product = get_object_or_404(Product, _id=product_id)
    data = request.data
    
    # update fields
    product.name=data['name'],
    product.description=data['description'],
    product.price=data['price'],
    product.count_in_stock=data['count_in_stock']
    
    product.save()
    
    serializer = ProductSerializer(product, many=False)
    
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product(request, product_id):
    product = get_object_or_404(Product, _id=product_id)
    product.delete()
    
    return Response('Product successfully deleted!')