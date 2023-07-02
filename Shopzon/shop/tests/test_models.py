from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import Category, Brand, Product

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.brand = Brand.objects.create(name='Test Brand', description='Test Description')
            
        self.product = Product.objects.create(
            user=self.user,
            category=self.category,
            brand=self.brand,
            name='Test Product',
            description='Test Description',
            rating=4.5,
            num_of_reviews=10,
            price=10.0,
            count_in_stock=100
        )
        
    def test_product_model(self):
        self.assertEqual(str(self.product), 'Test Product')