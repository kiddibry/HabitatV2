from django.db import models
from user.models import User


class HouseCategory(models.Model):
    name = models.CharField(max_length=255)


class House(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=999, blank=True)
    size = models.CharField(max_length=255)
    category = models.ForeignKey(HouseCategory, on_delete=models.CASCADE)
    on_sale = models.BooleanField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


class HouseImage(models.Model):
    image = models.CharField(max_length=999)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

