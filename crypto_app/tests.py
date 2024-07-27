from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Coin


class CoinTests(APITestCase):

    def setUp(self):
        self.coin = Coin.objects.create(
            coin_id="bitcoin", name="Bitcoin", symbol="BTC"
        )
        self.category = Category.objects.create(name="Test Category")
        self.category.coins.add(self.coin)
        self.user = User.objects.create_superuser(
            "testuser", "testuser@gmail.com", "password"
        )
        self.client.force_authenticate(user=self.user)

    def test_list_coins(self):
        url = reverse("coin-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_list_categories(self):
        url = reverse("category-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_coin(self):
        url = reverse("coin-detail", args=[self.coin.coin_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["coin_id"], self.coin.coin_id)

    def test_get_coins_by_category(self):
        url = reverse("coins-by-category", args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["coin_id"], self.coin.coin_id)




class HealthCheckTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            "testuser", "testuser@gmail.com", "password"
        )
        self.client.force_authenticate(user=self.user)

    def test_health_check(self):
        url = reverse("health-check")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "healthy")


class VersionTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            "testuser", "testuser@gmail.com", "password"
        )
        self.client.force_authenticate(user=self.user)

    def test_version_info(self):
        url = reverse("version-info")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["version"], "1.0")
        self.assertEqual(response.data["description"], "Crypto API")
