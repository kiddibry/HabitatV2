from django.db import models


class MerchCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=999)


class Merch(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(MerchCategory, on_delete=models.CASCADE)
    image = models.CharField(max_length=999)

