# Generated by Django 3.2 on 2021-10-04 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211004_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_modified',
        ),
    ]