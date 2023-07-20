from rest_framework import serializers
from .models import *

class BannerSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        
class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Gallery
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductGallerySerializer(many=True, required=False, allow_null=True)
    product_category = CategorySerilizer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        
