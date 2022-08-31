from django.db import models
from core.mixins.models import AuthorWithTimeMixin

class Category(models.Model):
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
       
       
       def __str__(self) -> str:
              return self.title
       
       class Meta:
              db_table = "products"