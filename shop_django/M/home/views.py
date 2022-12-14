from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')


class StoreView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home/index.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/product_detail.html', {'product': product})
