# Generated by Django 4.1.1 on 2022-12-12 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IProductive', '0004_day_day_profile_dayscompleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hobby',
            old_name='dailyTask',
            new_name='dailyHobby',
        ),
    ]
