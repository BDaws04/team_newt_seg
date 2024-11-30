# Generated by Django 5.1.2 on 2024-11-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0010_alter_session_end_day_alter_session_start_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_day',
            field=models.DateField(help_text='End date of the session term.'),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_day',
            field=models.DateField(help_text='Start date of the session term.'),
        ),
    ]
