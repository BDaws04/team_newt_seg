# Generated by Django 5.1.2 on 2024-11-23 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_programminglanguage_alter_course_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='course',
        ),
        migrations.AddField(
            model_name='session',
            name='programming_language',
            field=models.ForeignKey(default=1, help_text='Select the programming language for the session', on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='tutorials.programminglanguage'),
        ),
        migrations.AddField(
            model_name='session',
            name='season',
            field=models.CharField(choices=[('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer')], default='Fall', help_text='Select the season for the session', max_length=20),
        ),
        migrations.AddField(
            model_name='session',
            name='year',
            field=models.PositiveIntegerField(default=2024, help_text='Enter the year (e.g., 2024)'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
