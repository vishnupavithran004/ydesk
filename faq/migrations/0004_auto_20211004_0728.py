# Generated by Django 3.2 on 2021-10-04 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0003_auto_20211004_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='fk_created_user',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='date_modified',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='fk_modified_user',
            new_name='modified_by',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='fk_created_user',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='date_modified',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='fk_modified_user',
            new_name='modified_by',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='fk_created_user',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='date_modified',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='fk_modified_user',
            new_name='modified_by',
        ),
    ]
