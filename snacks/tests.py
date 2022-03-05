from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class MovieTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            name="twizzlers", purchaser=self.user, description="description test"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "twizzlers")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.name}", "twizzlers")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(f"{self.snack.description}", "description test")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "twizzlers")
        self.assertTemplateUsed(response, "snack-list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack-detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack-detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack-create"),
            {
                "name": "oreos",
                "purchaser": self.user.id,
                "description": "test",
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack-detail", args="2"))
        self.assertContains(response, "Details about oreos")
