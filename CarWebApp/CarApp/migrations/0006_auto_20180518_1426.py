# Generated by Django 2.0.4 on 2018-05-18 12:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0005_auto_20180518_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
