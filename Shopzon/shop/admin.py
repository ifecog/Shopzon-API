from django.contrib import admin
from .models import (
    Category, 
    Brand, 
    Product, 
    Review, 
    Order, 
    OrderItem,
    ShippingAddress
)
from django.utils.html import format_html

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name']

class BrandAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name', 'category', 'brand')
    list_filter = ('category', 'brand')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name', 'description', 'brand', 'category']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'rating', 'created_time')
    list_display_links = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('_id', 'created_time', 'is_paid', 'is_delivered')
    list_display_links = ['created_time']


class OrderItemAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'photo'
    
    list_display = ('_id', 'thumbnail', 'product', 'name', 'qty', 'price')
    list_display_links = ['thumbnail', 'name', 'product']


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('_id', 'country', 'city', 'postal_code')
    list_display_links = ['country']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
