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

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Extract the nested product_images data using 'pop' method
        product_images_data = validated_data.pop('product_images', [])

        # Create the main Product instance
        product = Product.objects.create(**validated_data)

        # Create the nested Product_Gallery instances if available
        for image_data in product_images_data:
            Product_Gallery.objects.create(product=product, **image_data)

        return product

class ReviewSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class CartSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
