import datetime
import os

from django.db import models


class Privilege(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'Privilege: {self.name}'


class Role(models.Model):
    name = models.CharField(max_length=128)
    privileges = models.ManyToManyField(Privilege)

    def __str__(self):
        return f'Role name: {self.name} - Privileges: {self.privileges.all()}'


class Person(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    email = models.CharField(max_length=128, null=False, blank=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'Person name: {self.name} - Password: {self.password} - ' \
               f'Email: {self.email} - Role: {self.role}'


def images_path():
    return os.path.join('images')


class Data(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'Data name: {self.name}'


class Example(models.Model):
    auto = models.AutoField(
        primary_key=True)
    number_big = models.BigIntegerField(
        null=False, blank=False)
    binary = models.BinaryField()
    boolean = models.BooleanField(default=True)
    char = models.CharField(
        max_length=65, null=False, blank=False)
    date = models.DateField(
        null=True, blank=True)
    date_time = models.DateTimeField(
        null=True, blank=True)
    decimal = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    duration = models.DurationField(
        default=datetime.timedelta, null=True, blank=True)
    email = models.EmailField()
    file = models.FileField(
        null=True, blank=True)
    float = models.FloatField()
    image = models.ImageField(
        null=True, blank=True)
    number = models.IntegerField()
    generic_ip_address = models.GenericIPAddressField()
    positive_number = models.PositiveIntegerField(
        null=True, blank=True)
    positive_small_number = models.PositiveSmallIntegerField(
        null=True, blank=True)
    positive_big_number = models.PositiveBigIntegerField(
        null=True, blank=True)
    slug = models.SlugField(
        max_length=25, null=True, blank=True)
    small_number = models.SmallIntegerField(
        null=True, blank=True)
    text = models.TextField(
        max_length=2500, null=True, blank=True)
    time_n = models.TimeField()
    url = models.URLField(null=True, blank=True)
    uu_id = models.UUIDField()
    foreign = models.ForeignKey(
        Person, on_delete=models.CASCADE)
    many_to_many = models.ManyToManyField(
        Privilege, blank=True)
    one_to_one = models.OneToOneField(
        Data, on_delete=models.CASCADE)
    json = models.JSONField()

    longitude = models.DecimalField(
        max_digits=23,
        decimal_places=20,
        blank=True,
        null=True
    )

    latitude = models.DecimalField(
        max_digits=23,
        decimal_places=20,
        blank=True,
        null=True
    )

    first_name = models.CharField(
        "Имя",
        max_length=30,
        default="",
        db_index=True
    )

    last_name = models.CharField(
        "Фамилия",
        max_length=56,
        default="",
        db_index=True
    )

    patronymic = models.CharField(
        "Отчество",
        max_length=56,
        default="",
        blank=True,
    )

    iin = models.CharField(
        "ИИН",
        max_length=12,
        unique=True,
        blank=True,
        null=True,
    )

    payment_amount = models.DecimalField(
        'Сумма платежей за все время',
        max_digits=20,
        decimal_places=3,
        default=0
    )

    # auto_big = models.BigAutoField()
    # auto_small = models.SmallAutoField()
    # null_boolean = models.NullBooleanField()
    # comma_separated_integer = models.CommaSeparatedIntegerField(max_length=128)
    # ip_address = models.IPAddressField()

    def __str__(self):
        return f'Example: email: {self.email} - Ip address: {self.generic_ip_address} - ' \
               f'Privilege: {self.many_to_many.all()}'















