from django.test import SimpleTestCase
from django.urls import resolve, reverse
from shop.views.product_views import (
    get_products, 
    get_toprated_products, 
    get_product_details,
    create_product_review,
    create_product,
)

class TestProductUrls(SimpleTestCase):
    def test_products_url_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, get_products)
        
    def test_toprated_products_url_is_resolved(self):
        url = reverse('toprated-products')
        self.assertEquals(resolve(url).func, get_toprated_products)
        
    def test_product_details_url_is_resolved(self):
        url = reverse('product-details', args=['some-slug'])
        self.assertEquals(resolve(url).func, get_product_details)
        
    def test_create_product_review_url_is_resolved(self):
        url = reverse('product-reviews', args=['some-slug'])
        self.assertEquals(resolve(url).func, create_product_review)
        
    def test_create_product_url_is_resolved(self):
        url = reverse('create-product')
        self.assertEquals(resolve(url).func, create_product)
        
    