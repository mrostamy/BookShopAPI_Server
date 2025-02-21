from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

from core.validators import validate_length
from django.core.validators import MinLengthValidator

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self, email=..., password=..., **extra_fields):

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("super user is staff must be True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("super user is superuser must be True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name="email", unique=True, null=False, blank=False
    )

    username = models.CharField(max_length=30, unique=True, blank=False, null=False)

    firstName = models.CharField(max_length=25, default="")
    lastName = models.CharField(max_length=35, default="")

    phoneNumber = models.CharField(validators=[validate_length], default="")

    address = models.TextField(default="")

    is_active=models.BooleanField(default=False)

    avatar=models.URLField(default="")

    objects = CustomUserManager()

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.username
