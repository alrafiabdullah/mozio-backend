from operator import mod
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Provider(models.Model):
    LANGUAGE_CHOICES = (
        ('bn', 'Bengali'),
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('pt', 'Portuguese'),
        ('ru', 'Russian'),
        ('ja', 'Japanese'),
        ('zh', 'Chinese'),
    )

    CURRENCY_CHOICES = (
        ('bdt', 'BDT'),
        ('usd', 'USD'),
        ('eur', 'EUR'),
        ('gbp', 'GBP'),
        ('cny', 'CNY'),
        ('jpy', 'JPY'),
        ('rub', 'RUB'),
    )

    name = models.CharField(max_length=100, default="")
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(default="")
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, default="bn")
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, default="bdt")

    def __str__(self):
        return self.name
