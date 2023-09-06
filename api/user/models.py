from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from .managers import CustomManager


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomManager()

    USERNAME_FIELD = "phone"

    def __str__(self):
        return self.phone

