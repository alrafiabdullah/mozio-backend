from django.db import models
from django.db.models.fields import CharField
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    phone_number = PhoneNumberField(default="")
    language = CharField(default="", max_length=50)
    currency = MoneyField(max_digits=1000, default=1.00,
                          decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.name
