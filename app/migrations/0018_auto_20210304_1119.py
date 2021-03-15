# Generated by Django 3.1.6 on 2021-03-04 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210304_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=23, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='example',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=23, verbose_name='Долгота'),
        ),
    ]
