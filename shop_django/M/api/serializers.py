from rest_framework import serializers
from accounts.models import User
from home.models import Product, Category


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'image', 'is_active', 'is_admin']


class ProfileEditSerializer(serializers.ModelSerializer):
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


class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
