from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    image = models.CharField(max_length=999, blank=True)
    created = models.DateTimeField()

