from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email successful"""
        email = 'shams@shams.com'
        password = 'Test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email of the user is normalized"""
        email = 'shams@SHAMSU.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='pasword1234',
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(None, "pass1234")

    def test_create_new_superuser(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_superuser(
            email='shams@SHAMSU.com',
            password='pasword1234',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
