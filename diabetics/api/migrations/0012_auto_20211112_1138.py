# Generated by Django 3.2.6 on 2021-11-12 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20211112_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predictionresult',
            old_name='decline',
            new_name='Aprroval',
        ),
        migrations.RenameField(
            model_name='predictionresult',
            old_name='done',
            new_name='reason',
        ),
    ]
