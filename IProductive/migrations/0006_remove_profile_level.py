# Generated by Django 4.1.1 on 2022-12-13 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IProductive', '0005_rename_dailytask_hobby_dailyhobby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='level',
        ),
    ]
