# Generated by Django 3.1.6 on 2021-03-04 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20210304_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='example',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='example',
            name='longitude',
        ),
    ]
