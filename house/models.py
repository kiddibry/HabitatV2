from django.db import models
from user.models import Profile


class HouseCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class House(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=999, blank=True)
    size = models.PositiveIntegerField()
    category = models.ForeignKey(HouseCategory, on_delete=models.CASCADE)
    postal_code = models.PositiveIntegerField()
    on_sale = models.BooleanField(default=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)


class HouseImage(models.Model):
    image = models.CharField(max_length=999)
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class HouseFilter(models.Model):
    ORDER_CHOICES = (
        ('name', 'Name lowest to highest'),
        ('-name', 'Name highest to lowest'),
        ('price', 'Price lowest to highest'),
        ('-price', 'Price highest to lowest'),
        ('size', 'Size lowest to highest'),
        ('-size', 'Size highest to lowest')
    )
    order = models.CharField(max_length=30, choices=ORDER_CHOICES, default='name')
    price_low = models.IntegerField(blank=True)
    price_high = models.IntegerField(blank=True)
    size_low = models.IntegerField(blank=True)
    size_high = models.IntegerField(blank=True)
