from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category_img = models.ImageField(upload_to="categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)  # Assign slugified category_name to slug field
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.category_name


    
class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)  # Assign slugified category_name to slug field
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.product_name

    
class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image")
    image = models.ImageField(upload_to="products")