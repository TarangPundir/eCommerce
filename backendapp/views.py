from django.shortcuts import get_object_or_404, render
from rest_framework import status
from .models import *
from .serilizers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# Banner API Starts
@api_view(['GET'])
def baneer_list(request):
    banner = Banner.objects.all()
    serializer = BannerSerilizer(banner, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def banner_create(request):
    serializer = BannerSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def banner_delete(request, id):
    banner = get_object_or_404(Banner, id=id)
    banner.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def banner_view(request, id):
    banner = Banner.objects.get(id=id)
    serializer = BannerSerilizer(banner, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def banner_update(request, id):
    banner = Banner.objects.get(id=id)
    serializer = BannerSerilizer(banner, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#Banner API Ends

# Category API starts
@api_view(['GET'])
def category_list(request):
    category = Category.objects.all()
    serializer = CategorySerilizer(category, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def category_create(request):
    serializer = CategorySerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def category_view(request, id):
    banner = Category.objects.get(id=id)
    serializer = CategorySerilizer(banner, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def category_update(request, id):
    category = Category.objects.get(id=id)
    serializer = CategorySerilizer(category, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

















































































































@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_view(request, id):
    products = Product.objects.get(id=id)
    serializer = ProductSerializer(products)
    return Response(serializer.data)

@api_view(['DELETE'])
def product_delete(request, id):
    product = Product.objects.get(id=id)
    product_gallery = Product_Gallery.objects.filter(product=product)
    product.delete()
    product_gallery.delete()
    return Response('success')
        