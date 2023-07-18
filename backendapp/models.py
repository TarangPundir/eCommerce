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
    