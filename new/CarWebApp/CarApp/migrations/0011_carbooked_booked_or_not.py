# Generated by Django 2.0.4 on 2018-05-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0010_auto_20180522_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbooked',
            name='booked_or_not',
            field=models.BooleanField(default=False),
        ),
    ]
