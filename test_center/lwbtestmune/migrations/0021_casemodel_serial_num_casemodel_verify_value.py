# Generated by Django 4.2.4 on 2023-09-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwbtestmune', '0020_alter_projectmodel_token_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='casemodel',
            name='serial_num',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='casemodel',
            name='verify_value',
            field=models.TextField(default=''),
        ),
    ]
