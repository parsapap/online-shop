from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from .serializers import ProfileSerializer, ProfileEditSerializer, ProductListSerializer, CategoryListSerializer, \
    ProductDetailSerializer, CommentCreateSerializer, CommentListSerializer, OrderItemSerializer, OrderSerializer
from rest_framework import status
from rest_framework import generics
from home.models import Product, Category, Comment
from orders.models import Order, OrderItem
from orders.cart import Cart


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
        ser_data = ProductDetailSerializer(instance=product)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class CommentCreateApiView(APIView):
    def post(self, request):
        user = request.user
        product = Product.objects.get(id=request.data['product'])
        ser_data = CommentCreateSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save(user=user, product=product)
            return Response(ser_data.data, status=status.HTTP_200_OK)

        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListApiView(generics.ListAPIView):
    queryset = Comment.objects.filter(is_reply=False)
    serializer_class = CommentListSerializer


class OrderCreateApiView(APIView):
    '''
        method post:
            for create order and save order in database
    '''

    def post(self, request):
        order = Order.objects.create(user=request.user)
        cart = Cart(request)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=float(item['price']),
                                     quantity=item['quantity'])
        cart.clear()
        ser_data = OrderSerializer(instance=order)
        result = ser_data.data
        result['message'] = 'order created'
        return Response(result, status=status.HTTP_200_OK)


class OrderDetailApiView(APIView):
    '''
        method get:
            for get order detail and show order items
    '''

    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        ser_data = OrderSerializer(instance=order)
        return Response(ser_data.data, status=status.HTTP_200_OK)
