# Generated by Django 4.2.2 on 2023-07-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0004_formentry_case_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='formentry',
            name='ncmr',
            field=models.CharField(default='', max_length=16),
        ),
    ]