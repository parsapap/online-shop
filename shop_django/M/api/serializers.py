from rest_framework import serializers
from accounts.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'image', 'is_active', 'is_admin']


class ProfileEditSerializer(serializers.ModelSerializer):
    model = User
    fields = ['full_name', 'email', 'phone_number', 'address']
