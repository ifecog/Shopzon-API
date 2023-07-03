from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from shop.models import Product, Order, OrderItem, ShippingAddress
from shop.serializers import OrderSerializer

from rest_framework import status

from datetime import datetime

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_order_items(request):
    user = request.user
    data = request.data
    
    orderItems = data['orderItems']
    if orderItems and len(orderItems) == 0:
        message = {'detail': 'No Order Items'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    else:
        # 1. create order
        order = Order.objects.create(
            user=user,
            payment_method=data['paymentMethod'],
            tax_price=data['taxPrice'],
            shipping_proce=data['shippingPrice'],
            total_price=data['totalPrice'],
        )
        # 2. create shipping address
        shipping_address = ShippingAddress.objects.create(
            order=order,
            country=data['shippingAddress']['country'],
            city=data['shippingAddress']['city'],
            address=data['shippingAddress']['address'],
            postal_code=data['shippingAddress']['postalCode']
        )
        # 3. create order items and set order to orderItem relationship
        for i in orderItems:
            product = get_object_or_404(Product, _id=i['product'])
            
            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i['qty'],
                price=i['price'],
                image=product.image.url
            )
            
            # 4. update stock
            product.count_in_stock -= item.qty
            product.save()
        
        serializer = OrderSerializer(order, many=False)
        return Response('Order!')