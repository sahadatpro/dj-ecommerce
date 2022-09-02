from email.policy import default
from django.db import models
from core.mixins.models import AuthorWithTimeMixin
from django.contrib.auth.models import User

class Customer(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
       name = models.CharField(max_length=200, null=True)
       email = models.CharField(max_length=200, null=True)
       
       def __str__(self) -> str:
              return self.name
       
class Category(AuthorWithTimeMixin):
       name = models.CharField(max_length=200)
       slug = models.SlugField(max_length=200, unique=True)
       
       def __str__(self) -> str:
              return self.name
       class Meta:
              db_table = "categories"
              
class Brand(AuthorWithTimeMixin):
       name = models.CharField(max_length=200)
       slug = models.SlugField(max_length=200, unique=True)
       
       def __str__(self):
              return self.name
       
       class Meta:
              db_table = "brands"

class Unit(AuthorWithTimeMixin):
       name = models.CharField(max_length=20)
       
       def __str__(self) -> str:
              return self.name
       
       class Meta:
              db_table = "units"

class Tag(AuthorWithTimeMixin):
       name = models.CharField(max_length=150)
       slug = models.SlugField(max_length=150)
       
       def __str__(self) -> str:
              return self.name
       
       class Meta:
              db_table = "tags"
       
class Product(AuthorWithTimeMixin):
       title = models.CharField(max_length=200)
       slug = models.SlugField(max_length=200, unique=True)
       meta = models.CharField(max_length=255, null=True, blank=True)
       
       category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
       brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
       unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
       tags = models.ManyToManyField(Tag, related_name="product_tags")
       
       description = models.TextField(null=True)
       price  = models.DecimalField(decimal_places=2, max_digits=5)
       digital = models.BooleanField(default=False, null=True, blank=True)
       #image = 
       
       
       def __str__(self) -> str:
              return self.title
       
       class Meta:
              db_table = "products"
              

class Order(models.Model):
       customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
       ordered_date = models.DateTimeField(auto_now_add=True)
       complete = models.BooleanField(default=False, blank=True, null=True)
       transaction_id = models.CharField(max_length=200, null=True)
       
       def __str__(self) -> str:
              return self.id 
       

class OrderItem(models.Model):
       product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
       order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
       quantity = models.IntegerField(default=0, null=True, blank=True)
       date_added = models.DateTimeField(auto_now_add=True)
       
class ShippingAddress(models.Model):
       customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
       order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
       address = models.CharField(max_length=100, null=True, blank=True)
       city = models.CharField(max_length=100, null=True, blank=True)
       state = models.CharField(max_length=100, null=True, blank=True)
       zipcode = models.CharField(max_length=100, null=True, blank=True)
       date_added = models.DateTimeField(auto_now_add=True)
       