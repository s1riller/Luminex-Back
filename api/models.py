# abstract_user/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    birth_date = models.DateField(null=True, blank=True)
    REQUIRED_FIELDS = ['birth_date']


class Imperfection(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class SkinType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name