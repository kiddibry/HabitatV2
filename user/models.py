from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    info = models.CharField(max_length=255, blank=True)
    is_admin = models.BooleanField(default=False)
    profile_image = models.CharField(max_length=999, blank=True)

    def __str__(self):
        return self.user.username

