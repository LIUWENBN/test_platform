# Generated by Django 4.2.4 on 2023-11-02 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lwbtestmune', '0022_alter_casemodel_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='casemodel',
            unique_together={('owner_business', 'case_name', 'url')},
        ),
    ]