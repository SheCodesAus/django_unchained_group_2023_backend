from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    username = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.username


