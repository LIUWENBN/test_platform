# Generated by Django 4.2.4 on 2023-09-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwbtestmune', '0002_projectmodel_project_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
