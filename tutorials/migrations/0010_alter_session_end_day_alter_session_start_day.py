# Generated by Django 5.1.2 on 2024-11-29 10:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0009_rename_is_availble_session_is_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]