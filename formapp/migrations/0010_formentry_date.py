# Generated by Django 4.2 on 2023-08-19 23:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0009_remove_formentry_file_filesentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='formentry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 16, 50, 14, 862068)),
        ),
    ]
