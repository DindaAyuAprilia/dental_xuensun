from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError("Email harus diisi")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser):
    DOKTER = 1
    PASIEN = 2
    ROLE_CHOICES = (
        (DOKTER, 'Dokter'),
        (PASIEN, 'Pasien'),
    )

    email = models.EmailField(unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    objects = UsersManager()

    def __str__(self):
        return self.email
