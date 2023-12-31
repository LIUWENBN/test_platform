# Generated by Django 4.2.4 on 2023-09-12 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lwbtestmune', '0007_alter_businessmodel_owner_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=20)),
                ('relation', models.CharField(default='', max_length=200)),
                ('relation_key', models.CharField(default='', max_length=100)),
                ('is_run', models.CharField(max_length=20)),
                ('header', models.TextField(default='', max_length=200)),
                ('method', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('data', models.TextField()),
                ('exp_result', models.TextField()),
                ('real_result', models.TextField()),
                ('verify_type', models.CharField(max_length=20)),
                ('is_pass', models.CharField(default='', max_length=20)),
                ('case_info', models.TextField(default='', max_length=100)),
                ('owner_business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case', to='lwbtestmune.businessmodel')),
                ('owner_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case', to='lwbtestmune.projectmodel')),
            ],
        ),
    ]
