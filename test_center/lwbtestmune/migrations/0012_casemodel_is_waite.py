# Generated by Django 4.2.4 on 2023-09-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwbtestmune', '0011_remove_casemodel_is_run_casemodel_case_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='casemodel',
            name='is_waite',
            field=models.CharField(default='', max_length=6),
        ),
    ]
