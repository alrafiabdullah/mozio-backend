# Generated by Django 3.2.6 on 2021-08-17 13:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210817_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.provider')),
            ],
        ),
    ]
