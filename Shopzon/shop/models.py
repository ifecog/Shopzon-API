from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='categories/%y/%m/%d/', blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='brands/%y/%m/%d/', blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(
        upload_to='products/%y/%m/%d/', null=True, blank=True, default='/placeholder.png')
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    num_of_reviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    count_in_stock = models.IntegerField(null=True, blank=True, default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    tax_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    payment_time = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivery_time = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.user.first_name


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class ShippingAddress(models.Model):
    state_choice = (
        # Africa
        ('NG', 'Nigeria'),
        ('GH', 'Ghana'),
        ('EG', 'Egypt'),
        ('ZA', 'South Africa'),
        ('ET', 'Ethiopia'),
        ('DZ', 'Algeria'),

        # Asia
        ('CN', 'China'),
        ('IN', 'India'),
        ('JP', 'Japan'),
        ('VN', 'Vietnam'),
        ('TH', 'Thailand'),
        ('KR', 'South Korea'),

        # Europe
        ('RU', 'Russia'),
        ('DE', 'Germany'),
        ('FR', 'France'),
        ('GB', 'United Kingdom'),
        ('IT', 'Italy'),
        ('ES', 'Spain'),
        ('PL', 'Poland'),
        ('NL', 'Netherlands'),
        ('BE', 'Belgium'),
        ('SE', 'Sweden'),

        # North America
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('MX', 'Mexico'),

        # Oceania
        ('AU', 'Australia'),
        ('NZ', 'New Zealand'),
        ('FJ', 'Fiji'),
        ('PG', 'Papua New Guinea'),
        
        # South America
        ('BR', 'Brazil'),
        ('AR', 'Argentina'),
        ('CO', 'Colombia'),
        ('PE', 'Peru'),
        ('CL', 'Chile'),
        ('VE', 'Venezuela'),
        ('EC', 'Ecuador'),
        ('BO', 'Bolivia'),
        ('PY', 'Paraguay'),
        ('UY', 'Uruguay'),

    )
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(choices=state_choice, max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'shipping address'
        verbose_name_plural = 'shipping addresses'
