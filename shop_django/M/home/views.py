from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product

class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')


class StoreView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/index.html', {'products': products})
