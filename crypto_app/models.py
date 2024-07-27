from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Coin(models.Model):
    coin_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    categories = models.ManyToManyField(Category, related_name="coins")
