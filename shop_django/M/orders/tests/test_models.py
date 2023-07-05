from django.test import TestCase
from ..models import Order, OrderItem, Coupon
from accounts.models import User
from home.models import Product, Category


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='parsa@gmail.com', full_name='parsa', phone_number='09123456789',
                                             password='123456')
        self.order = Order.objects.create(user=self.user, paid=True, discount=0)

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertTrue(self.order.paid)
        self.assertEqual(self.order.discount, 0)

    def test_order_str(self):
        self.assertEqual(str(self.order), 'parsa - 1')


class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='parsa@gmail.com', full_name='parsa', phone_number='09123456789',
                                             password='123456')
        self.order = Order.objects.create(user=self.user, paid=True, discount=0)
        self.category = Category.objects.create(name='django', slug='django')
        self.product = Product.objects.create(category=self.category, name='django beginners', slug='django-beginners',
                                              description='django beginners', price=20.00, available=True)
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, price=20, quantity=1)

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.price, 20)
        self.assertEqual(self.order_item.quantity, 1)

    def test_order_item_str(self):
        self.assertEqual(str(self.order_item), '1')


class CouponModelTest(TestCase):
    def setUp(self):
        self.coupon = Coupon.objects.create(code='parsa', valid_from='2021-01-01', valid_to='2021-01-01', discount=0,
                                            active=True)

    def test_coupon_creation(self):
        self.assertEqual(self.coupon.code, 'parsa')
        self.assertEqual(self.coupon.valid_from, '2021-01-01')
        self.assertEqual(self.coupon.valid_to, '2021-01-01')
        self.assertEqual(self.coupon.discount, 0)
        self.assertTrue(self.coupon.active)

    def test_coupon_str(self):
        self.assertEqual(str(self.coupon), 'parsa')
