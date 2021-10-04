# Generated by Django 3.2 on 2021-10-04 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20211004_0643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='char_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='char_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='fk_organization',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='char_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='char_name',
            new_name='name',
        ),
    ]