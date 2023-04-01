from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModalTests(TestCase):
    def test_create_user_with_email_successfull(self):
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"]
        ]

        for email, expected in sample:
            user = get_user_model().objects.create_user(email=email)
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "sample")

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        user = get_user_model().objects\
            .create_user("test@example.com", "testpass123")
        recipe = models.Recipe.objects.create(
            user=user,
            title="sample recipe name",
            time_minutes=5,
            price=Decimal("5.50"),
            description="Sample recipe description",
        )

        self.assertEqual(str(recipe), recipe.title)
