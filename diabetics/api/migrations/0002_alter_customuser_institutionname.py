# Generated by Django 3.2.6 on 2021-11-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='InstitutionName',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
