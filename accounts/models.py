from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True, blank=True)

    def __str__(self):
        return self.username
