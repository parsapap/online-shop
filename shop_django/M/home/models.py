from django.db import models
from django.urls import reverse
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_detail', args=[self.slug])


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pcomments')
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'
