from django.db import models
from user.models import Profile 


class HouseCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class House(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=999, blank=True)
    size = models.CharField(max_length=255)
    category = models.ForeignKey(HouseCategory, on_delete=models.CASCADE)
    on_sale = models.BooleanField(default=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)


class HouseImage(models.Model):
    image = models.CharField(max_length=999)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

