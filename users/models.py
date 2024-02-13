from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    surname2 = models.CharField(max_length=50, verbose_name='Отчество', **NULLABLE)
    address = models.CharField(max_length=250, verbose_name='Адрес')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    phone = PhoneNumberField(unique=True, verbose_name='Номер телефона', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
