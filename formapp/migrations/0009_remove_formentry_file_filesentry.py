# Generated by Django 4.2 on 2023-07-17 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0008_alter_formentry_insp_report_if_rej_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formentry',
            name='file',
        ),
        migrations.CreateModel(
            name='FilesEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='%Y%m%d-%H%M%S')),
                ('associated_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formapp.formentry')),
            ],
        ),
    ]
