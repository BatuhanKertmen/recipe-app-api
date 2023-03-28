from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects\
            .create_superuser("admin@example.com", "admintest123")
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects\
            .create_user("user@example.com", "testpass123", name="tester")

    def test_users_list(self):
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
