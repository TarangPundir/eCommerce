from django.db import models

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banner', height_field=None, width_field=None, max_length=None)
    banner_text = models.CharField(max_length=500)
    
        
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_parent = models.ForeignKey("backendapp.Category",  on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.category_name

    # Shivam code
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    long_description = models.TextField(max_length=1000)
    product_price = models.IntegerField()
    product_discount = models.IntegerField()
    product_thumbnail = models.ImageField(upload_to='product_thumbnail', null=True, blank=True)
    product_category = models.ManyToManyField("backendapp.Category", null=True, blank=True)
    def __str__(self):
        return self.product_name
    
class Product_Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images', null=True, blank=True)
    image = models.ImageField(upload_to='product_gallery')