# Generated by Django 4.2.4 on 2023-09-17 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lwbtestmune', '0016_rename_project_url_projectmodel_project_base_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmodel',
            old_name='project_base_url',
            new_name='base_url',
        ),
        migrations.RenameField(
            model_name='projectmodel',
            old_name='project_login_url',
            new_name='login_url',
        ),
    ]
