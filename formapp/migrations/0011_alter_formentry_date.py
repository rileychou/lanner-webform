# Generated by Django 4.2 on 2023-08-19 23:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0010_formentry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formentry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 16, 51, 34)),
        ),
    ]
