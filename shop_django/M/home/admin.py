from django.contrib import admin
from .models import Category, Product, Comment
from core.admin import BaseAdmin


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'is_active', 'is_deleted']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug']
    raw_id_fields = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Comment)
class CommentAdmin(BaseAdmin):
    list_display = ['user', 'product', 'created', 'updated', 'is_active', 'is_deleted']
