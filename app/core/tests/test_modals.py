from django.test import TestCase
from django.contrib.auth import get_user_model


class ModalTests(TestCase):

    def test_crete_user_with_email_successfull(self):
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
