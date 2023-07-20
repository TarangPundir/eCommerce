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

# Shivam
@api_view(["GET"])
def category_child(request, id):
    category = Category.objects.filter(category_parent=id)
    serializers=CategorySerilizer(category, many=True)
    return Response(serializers.data)



@api_view(["GET"])
def parent_model_by_child_id(request, child_id):
    try:
        parents = Category.objects.filter(child_model__id=child_id)
        serializer = CategorySerilizer(parents, many=True)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response({"error": "ParentModel not found"}, status=404)



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


# Shivam
@api_view(["GET"])
def review_list(request):
    review = Review.objects.all()
    serializers = ReviewSerilizer(review, many=True)
    return Response(serializers.data)

@api_view(["POST"])
def review_create(request):
    serializers = ReviewSerilizer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def review_view(request, id):
    review = Review.objects.get(id=id)
    serializers = ReviewSerilizer(review, many=False)
    return Response(serializers.data)

@api_view(['DLETE'])
def review_delete(request, id):
    review = get_object_or_404( Review ,id=id)
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)