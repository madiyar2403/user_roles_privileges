# Generated by Django 3.1.6 on 2021-02-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210225_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='many_to_many',
            field=models.ManyToManyField(blank=True, to='app.Privilege'),
        ),
    ]