# Generated by Django 4.1.7 on 2023-06-09 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("konta", "0002_usermodel_profile_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usermodel",
            name="profile_picture",
        ),
    ]
