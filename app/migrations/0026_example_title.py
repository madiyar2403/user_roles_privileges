# Generated by Django 3.1.6 on 2021-03-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_example_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='title',
            field=models.CharField(default='', max_length=128, unique=True, verbose_name='Название'),
        ),
    ]
