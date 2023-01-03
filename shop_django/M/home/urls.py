from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('store/', views.StoreView.as_view(), name='store'),
    path('category/<slug:category_slug>/', views.StoreView.as_view(), name='category_filter'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),

]
