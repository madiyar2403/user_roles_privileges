# Generated by Django 3.1.6 on 2021-02-24 15:01

import app.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210223_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('auto', models.AutoField(primary_key=True, serialize=False)),
                ('number_big', models.BigIntegerField()),
                ('binary', models.BinaryField()),
                ('boolean', models.BooleanField()),
                ('char', models.CharField(max_length=65)),
                ('date', models.DateField()),
                ('date_time', models.DateTimeField()),
                ('decimal', models.DecimalField(decimal_places=5, max_digits=10)),
                ('duration', models.DurationField()),
                ('email', models.EmailField(max_length=254)),
                ('file', models.FileField(upload_to='')),
                ('file_path', models.FilePathField(path=app.models.images_path)),
                ('float', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('number', models.IntegerField()),
                ('generic_ip_address', models.GenericIPAddressField()),
                ('positive_number', models.PositiveIntegerField()),
                ('positive_small_number', models.PositiveSmallIntegerField()),
                ('positive_big_number', models.PositiveBigIntegerField()),
                ('slug', models.SlugField(max_length=25)),
                ('small_number', models.SmallIntegerField()),
                ('text', models.TextField(max_length=250)),
                ('time', models.TimeField()),
                ('url', models.URLField()),
                ('uu_id', models.UUIDField(default=uuid.uuid4)),
                ('json', models.JSONField()),
                ('foreign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
                ('many_to_many', models.ManyToManyField(to='app.Privilege')),
                ('one_to_one', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.data')),
            ],
        ),
    ]
