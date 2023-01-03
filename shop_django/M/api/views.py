from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from .serializers import ProfileSerializer, ProfileEditSerializer, ProductListSerializer, CategoryListSerializer, ProductDetailSerializers
from rest_framework import status
from rest_framework import generics
from home.models import Product, Category


# account app api views
class ProfileApiView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        ser_data = ProfileSerializer(instance=user)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class ProfileEditApiView(APIView):
    def put(self, request, user_id):
        user = User.objects.get(id=user_id)
        ser_data = ProfileEditSerializer(instance=user, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductListSerializer


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ProductDetailApiView(APIView):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        ser_data = ProductDetailSerializers(instance=product)
        return Response(ser_data.data, status=status.HTTP_200_OK)
