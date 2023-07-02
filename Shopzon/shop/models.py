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
