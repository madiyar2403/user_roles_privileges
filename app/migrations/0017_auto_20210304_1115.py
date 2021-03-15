# Generated by Django 3.1.6 on 2021-03-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210301_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='latitude',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=20, default=None, max_digits=23, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='example',
            name='longitude',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=20, default=None, max_digits=23, verbose_name='Долгота'),
        ),
    ]