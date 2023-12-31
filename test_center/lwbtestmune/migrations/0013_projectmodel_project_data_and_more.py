# Generated by Django 4.2.4 on 2023-09-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwbtestmune', '0012_casemodel_is_waite'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='project_data',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='project_header',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='project_login_url',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='project_method',
            field=models.CharField(default='GET', max_length=20),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='project_token',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='project_url',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='casemodel',
            name='data',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='casemodel',
            name='exp_result',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='casemodel',
            name='real_result',
            field=models.TextField(default=''),
        ),
        migrations.AlterUniqueTogether(
            name='casemodel',
            unique_together={('case_name', 'owner_project', 'owner_business')},
        ),
    ]
