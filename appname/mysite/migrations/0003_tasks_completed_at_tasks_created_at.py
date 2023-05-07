# Generated by Django 4.2 on 2023-05-05 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_rename_task_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
