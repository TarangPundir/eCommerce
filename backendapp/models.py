from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banner', height_field=None, width_field=None, max_length=None)
    banner_text = models.CharField(max_length=500)
    
        
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_parent = models.ForeignKey("backendapp.Category",  on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.category_name
    
      
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    long_description = models.TextField(max_length=1000)
    product_price = models.IntegerField()
    product_discount = models.IntegerField()
    product_thumbnail = models.ImageField(upload_to='product_thumbnail', null=True, blank=True)
    product_category = models.ManyToManyField("backendapp.Category", blank=True)
    def __str__(self):
        return self.product_name
    
class Product_Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images', null=True, blank=True)
    image = models.ImageField(upload_to='product_gallery')

Expreyance = (
    ("Good","Good"),
    ("Average", "Average"),
    ("Best", "Best"),
    ("Bad", "Bad"),
    ("Worst", "Worst"),
)

class Review(models.Model):
    rating = models.FloatField()
    expreyance = models.CharField(max_length=100, choices=Expreyance, default=1) 
    file = models.FileField()
    description = models.TextField(max_length=500)
    product_name = models.CharField(max_length=100)
    
class Cart(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    product = models.ForeignKey("backendapp.Product", verbose_name=_("product_fk_id"), on_delete=models.CASCADE)
    count = models.IntegerField()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
