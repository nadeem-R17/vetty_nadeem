# from django.db import models

# class Coin(models.Model):
#     coin_id = models.CharField(max_length=100, unique=True)
#     name = models.CharField(max_length=100)
#     symbol = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name
    

# class Category(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     coins = models.ManyToManyField(Coin, related_name='categories')


# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Coin(models.Model):
    coin_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    categories = models.ManyToManyField(Category, related_name='coins')
