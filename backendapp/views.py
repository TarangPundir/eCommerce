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


@api_view(['POST'])
def save_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        product = serializer.save()

        # Assuming you have received category IDs in the 'product_category' field of the request data
        category_ids = request.data.get('product_category', [])

        # Clear existing categories and set the related categories using .set() method
        product.product_category.clear()
        product.product_category.set(category_ids)

        product_gallery_data = request.data.get('product_images')
        if product_gallery_data:
            for image_data in product_gallery_data:
                image_serializer = ProductGallerySerializer(data=image_data)
                if image_serializer.is_valid():
                    image_serializer.save(product=product)
                else:
                    return Response(image_serializer.errors, status=400)

        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

        
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

@api_view(['GET'])
def cart_list(request):
    try:
        cart = Cart.objects.all()
        serializer = CartSerilizer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error":"cart not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def cart_store(request):
    serializers = CartSerilizer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def cart_view(request, id):
    try:
        cart = Cart.objects.get(id=id)
    except Cart.DoesNotExist:
        return Response({"error":"Product not found"}, status=status.HTTP_404_NOT_FOUND)
    serilizer = CartSerilizer(cart)
    return Response(serilizer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def cart_delete(request, id):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def cart_update(request, id):
    try:
        cart = Cart.objects.get(id=id)
    except Cart.DoesNotExist:
        return Response({"error":"cart not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = CartSerilizer(cart, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def contact_list(request):
    try:
        contact = Contact.objects.all()
    except Contact.DoesNotExist:
        return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ContactSerilizer(contact, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def contact_view(request, id):
    contact = get_object_or_404(Contact, id=id)
    serializer = ContactSerilizer(contact)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def contact_store(request):
    serilizer = ContactSerilizer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data, status=status.HTTP_201_CREATED)
    return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def contact_update(request, id):
    contact = get_object_or_404(Contact, id=id)
    serializer = ContactSerilizer(contact, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def product_search(request):
    product = request.data.get('name')
    if not product:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    searched = Product.objects.filter(product_name__icontains=product)
    if not searched:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serilizer = ProductSerializer(searched, many=True)
    return Response(serilizer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def category_search(request):
    search = request.data.get('name')
    if not search:
        return Response({"error":"correct the code"}, status=status.HTTP_400_BAD_REQUEST)
    category = Category.objects.filter(category_name__icontains=search)
    if not category:
        return Response({"error":"Nothing match with your search"}, status=status.HTTP_404_NOT_FOUND    )
    serilizer = CategorySerilizer(category, many=True)
    return Response(serilizer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def category_product(request):
    category_ids = request.data.get('name', [])
    if not category_ids:
        products = Product.objects.all()
        if not products:
            return Response({"error":"no products"}, status=status.HTTP_404_NOT_FOUND)
    else:
        products = Product.objects.filter(product_category__in=category_ids).distinct()
        if not products:
            return Response({"error":"nothing matches"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def product_under_price(request):
    search = request.data.get('price')
    if not search:
        return Response({"error":"contact"}, status=status.HTTP_400_BAD_REQUEST)
    product = Product.objects.filter(product_price__lte=search)
    if not product:
        return Response({"error":"nothing found"}, status=status.HTTP_404_NOT_FOUND)
    serilizer = ProductSerializer(product, many=True)
    return Response(serilizer.data, status=status.HTTP_200_OK)
    
        

