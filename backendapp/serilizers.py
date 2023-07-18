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