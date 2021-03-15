from factory import SubFactory
from factory.django import DjangoModelFactory
from app.models import Person, Role, Privilege, Data, Example
from random import randrange, uniform, choice
from faker import Faker
import factory
import datetime
import pytz

fake = Faker('ru_RU')


class PrivilegeFactory(DjangoModelFactory):
    class Meta:
        model = Privilege

    name = fake.word()


class RoleFactory(DjangoModelFactory):
    class Meta:
        model = Role

    name = fake.job()

    @factory.post_generation
    def privileges(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for privilege in extracted:
                self.privileges.add(privilege)


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    name = fake.name()
    password = fake.password(length=12)
    email = fake.email()
    role = SubFactory(RoleFactory)


class DataFactory(DjangoModelFactory):
    class Meta:
        model = Data

    name = fake.address()


class ExampleFactory(DjangoModelFactory):
    class Meta:
        model = Example

    number_big = fake.bothify('%############')
    binary = fake.binary(length=64)
    boolean = fake.boolean()
    char = fake.word()
    date = fake.date()
    date_time = fake.date_time(tzinfo=pytz.UTC)
    decimal = fake.bothify('%###.#######')
    duration = datetime.timedelta(days=int(fake.bothify('%')), hours=int(fake.bothify('%#')))
    email = fake.email()
    file = fake.file_name()
    float = float(fake.bothify('%###.###'))
    image = fake.bothify('?????????.jpg')
    number = fake.random_digit()
    generic_ip_address = fake.ipv4()
    positive_number = fake.bothify('%##########')
    positive_small_number = fake.bothify('%#%#%')
    positive_big_number = fake.bothify('%##############')
    slug = fake.bothify('?????-?????')
    small_number = fake.random_digit()
    text = fake.paragraph(nb_sentences=10, variable_nb_sentences=False)
    time_n = fake.time()
    url = fake.url()
    uu_id = fake.uuid4()
    foreign = SubFactory(PersonFactory)
    # foreign_id = 1
    # latitude = factory.LazyAttribute(lambda a: uniform(-90, +90))
    # longitude = factory.LazyAttribute(lambda a: uniform(-180, +180))
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    # first_name = fake.first_name_nonbinary()
    # last_name = fake.last_name_nonbinary()
    # patronymic = fake.middle_name_nonbinary()
    first_name = factory.Faker('first_name_nonbinary')
    last_name = factory.Faker('last_name_nonbinary')
    patronymic = factory.Faker('last_name_nonbinary')
    iin = factory.LazyAttribute(lambda a: '{:0>12}'.format(randrange(999999999999)))

    @factory.post_generation
    def many_to_many(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for many_to_manys in extracted:
                self.many_to_many.add(many_to_manys)

    one_to_one = SubFactory(DataFactory)
    json = fake.json(num_rows=1)


