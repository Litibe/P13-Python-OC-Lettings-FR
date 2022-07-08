from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=8)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True, default=None)

    def __str__(self):
        return self.user.username
