# Generated by Django 3.1.6 on 2021-02-24 15:26

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_data_example'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='file_path',
            field=models.FilePathField(blank=True, null=True, path=app.models.images_path),
        ),
    ]
