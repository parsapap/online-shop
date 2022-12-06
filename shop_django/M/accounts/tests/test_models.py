from django.test import TestCase
from ..models import User, OtpCode


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='parsa@gmail.com', full_name='parsa', phone_number='09123456789',
                                             password='123456')

    def test_user_create(self):
        self.assertEqual(self.user.email, 'parsa@gmail.com')
        self.assertEqual(self.user.full_name, 'parsa')
        self.assertEqual(self.user.phone_number, '09123456789')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_admin)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'parsa@gmail.com')

    def test_user_has_perm(self):
        self.assertTrue(self.user.has_perm('account.add_user'))
        self.assertTrue(self.user.has_perm('account.change_user'))
        self.assertTrue(self.user.has_perm('account.delete_user'))
        self.assertTrue(self.user.has_perm('account.view_user'))

    def test_user_has_module_perms(self):
        self.assertTrue(self.user.has_module_perms('account'))

    def test_user_is_staff(self):
        self.assertFalse(self.user.is_staff)

    def test_user_is_superuser(self):
        self.assertFalse(self.user.is_superuser)


class OtpCodeTestCase(TestCase):
    def setUp(self):
        self.otp_code = OtpCode.objects.create(phone_number='09123456789', code=123456)

    def test_otp_code_create(self):
        self.assertEqual(self.otp_code.phone_number, '09123456789')
        self.assertEqual(self.otp_code.code, 123456)

    def test_otp_code_str(self):
        self.assertEqual(str(self.otp_code), '09123456789 - 123456 - 2020-11-22 19:20:28.574000+00:00')
