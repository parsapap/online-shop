from django.contrib import admin
from .models import Order, OrderItem, Coupon
from core.admin import BaseAdmin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(BaseAdmin):
    list_display = ('id', 'user', 'updated', 'paid', 'created', 'updated', 'is_deleted')
    list_filter = ('paid',)
    inlines = (OrderItemInline,)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'valid_from', 'valid_to', 'discount', 'active')
    list_filter = ('active', 'valid_from', 'valid_to')
    search_fields = ('code',)
