# Generated by Django 3.2.6 on 2021-08-17 13:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_provider_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='currency',
            field=models.CharField(choices=[('bdt', 'BDT'), ('usd', 'USD'), ('eur', 'EUR'), ('gbp', 'GBP'), ('cny', 'CNY'), ('jpy', 'JPY'), ('rub', 'RUB')], max_length=3),
        ),
        migrations.AlterField(
            model_name='provider',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='provider',
            name='language',
            field=models.CharField(choices=[('bn', 'Bengali'), ('en', 'English'), ('es', 'Spanish'), ('fr', 'French'), ('de', 'German'), ('it', 'Italian'), ('pt', 'Portuguese'), ('ru', 'Russian'), ('ja', 'Japanese'), ('zh', 'Chinese')], max_length=2),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='provider',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]