from django.test import TestCase
from ..models import Category, Product


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='django', slug='django')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'django')
        self.assertEqual(self.category.slug, 'django')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'django')


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='django', slug='django')
        self.product = Product.objects.create(category=self.category, name='django beginners', slug='django-beginners',
                                              description='django beginners', price=20.00, available=True)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'django beginners')
        self.assertEqual(self.product.slug, 'django-beginners')
        self.assertEqual(self.product.description, 'django beginners')
        self.assertEqual(self.product.price, 20.00)
        self.assertEqual(self.product.available, True)

    def test_product_str(self):
        self.assertEqual(str(self.product), 'django beginners')

    def test_product_get_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url(), '/django-beginners/')
