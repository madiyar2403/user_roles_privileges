# Generated by Django 3.1.6 on 2021-02-24 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210224_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='example',
            old_name='time',
            new_name='time_n',
        ),
        migrations.AlterField(
            model_name='example',
            name='text',
            field=models.TextField(max_length=2500),
        ),
    ]
