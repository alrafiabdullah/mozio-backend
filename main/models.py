from django.contrib.gis.db import models
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

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES)
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.PolygonField()

    def __str__(self):
        return self.name
