# Generated by Django 4.2.2 on 2023-06-30 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formentry',
            name='nonconf_quantity',
        ),
        migrations.RemoveField(
            model_name='formentry',
            name='tot_lot_size',
        ),
    ]