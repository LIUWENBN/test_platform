# Generated by Django 4.2.4 on 2023-09-17 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lwbtestmune', '0018_projectmodel_token_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodel',
            name='project_token',
        ),
    ]
