# Generated by Django 4.1.1 on 2022-12-11 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IProductive', '0003_rename_tasks_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='day',
            field=models.PositiveSmallIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='daysCompleted',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
