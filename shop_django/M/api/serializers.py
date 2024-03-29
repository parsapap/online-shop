from rest_framework import serializers
from accounts.models import User
from home.models import Product, Category, Comment
from orders.models import Order, OrderItem


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'image', 'is_active', 'is_admin']


class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'address']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image', 'category', 'description', 'available']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'is_sub', 'sub_category']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['user', 'product', 'reply', 'is_reply', 'body']

    def get_user(self, obj):
        return obj.user.full_name


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'product', 'reply', 'is_reply', 'body']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('order_items', 'user', 'paid', 'discount')

    def get_order_items(self, obj):
        order_items = obj.items.all()
        return OrderItemSerializer(order_items, many=True).data
