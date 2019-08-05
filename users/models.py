from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
# Create your models here.


"""
Добавление нового пользователя
"""
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)  # Поле регистрации при помощи Email
    is_staff = models.BooleanField(default=False)  # Есть ли у пользователя права разработчика
    is_active = models.BooleanField(default=True)  #
    date_joined = models.DateTimeField(default=timezone.now)  # Время когда присоединился данный пользователь

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

