from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'test@faz13.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual((user.email), email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the mail for a new user is normalized"""
        email = 'test@FAZ13.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invaild_email(self):
        """Test creating new user with a invaild email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@superuser.com',
            'test123'
        )
        # 'is_superuser' is part of Permission mixin
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
