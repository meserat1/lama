# Generated by Django 3.2.6 on 2021-11-12 07:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20211112_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinformation',
            name='user',
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
