from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not email:
            raise AttributeError("User must set an email address")
        else:
            # normalizes the provided email
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a new superuser using an email address"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not email:
            raise AttributeError("User must set an email address")
        else:
            # normalizes the provided email
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email Address', max_length=255, unique=True,
        blank=False, null=True
    )
    is_staff = models.BooleanField(
        verbose_name='Staff status', default=False, null=True
    )
    is_active = models.BooleanField(
        verbose_name='Active', default=True, null=True
    )
    date_joined = models.DateTimeField(
        verbose_name='Date Joined', auto_now_add=True, null=True
    )
    last_updated = models.DateTimeField(
        verbose_name='Last Updated', auto_now=True, null=True
    )

    # uses the custom manager
    objects = UserManager()

    # overrides username to email field according to the Story
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
