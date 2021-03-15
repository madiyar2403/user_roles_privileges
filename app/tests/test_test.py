import pytest
import requests
from faker import Faker

from app.example import get_boolean

fake = Faker()

'''Testing privileges'''


def test_create_privilege_status_created(test_client, db):
    data = {
        'name': fake.word()
    }
    req = test_client.post('/privilege/', data)
    assert req.status_code == 201
    assert 'name' in data
    assert req.json() == req.json()


def test_create_privilege_status_bad_request(test_client, db):
    data = {}
    req = test_client.post('/privilege/', data)
    assert req.status_code == 400
    assert req.json() == {'name': ['This field is required.']}
    assert req.json() == req.json()


def test_view_privileges_status_ok(test_client, test_privilege):
    r = test_client.get('/privilege/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_privileges_status_not_found(test_client, test_privilege):
    with pytest.raises(ValueError):
        r = test_client.get('/privileges/')
        assert r.status_code == 404
        assert r.json() == r.json()


def test_view_privilege_detail_status_ok(test_client, test_privilege):
    r = test_client.get(f'/privilege/{test_privilege.id}/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_privilege_detail_does_not_exist(test_client, test_privilege):
    r = test_client.get(f'/privilege/{10005000}/')
    assert r.status_code == 404


def test_update_privilege_detail_status_ok(test_client, test_privilege):
    r = test_client.put(f'/privilege/{test_privilege.id}/',
                        {"name": "123456"})
    assert r.status_code == 200
    d = r.json()
    assert d.get('name') == '123456'


def test_update_privilege_detail_status_not_ok(test_client, test_privilege):
    r = test_client.put(f'/privilege/{10005000}/', {"name": "123456"})
    assert r.status_code == 404


def test_delete_privilege_detail_status_ok(test_client, test_privilege):
    r = test_client.delete(f'/privilege/{test_privilege.id}/')
    assert r.status_code == 204


def test_delete_privilege_detail_does_not_exist(test_client, test_privilege):
    r = test_client.delete(f'/privilege/{10005000}/')
    assert r.status_code == 404


'''Testing roles'''


def test_create_role_status_created(test_client, test_privilege, db):
    data = {
        'name': fake.job(),
        'privileges': test_privilege.id
    }
    req = test_client.post('/role/', data)
    assert req.status_code == 201
    assert 'name' in data
    assert req.json() == req.json()


def test_create_role_status_bad_request(test_client, db):
    data = {}
    req = test_client.post('/role/', data)
    assert req.status_code == 400
    assert req.json() == \
           {'name': ['This field is required.'],
            'privileges': ['This list may not be empty.']}
    assert req.json() == req.json()


def test_view_roles_status_ok(test_client, test_role):
    r = test_client.get('/role/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_roles_status_not_found(test_client, test_role):
    with pytest.raises(ValueError):
        r = test_client.get('/roles/')
        assert r.status_code == 404
        assert r.json() == r.json()


def test_view_role_detail_status_ok(test_client, test_role):
    r = test_client.get(f'/role/{test_role.id}/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_role_detail_does_not_exist(test_client, test_role):
    r = test_client.get(f'/role/{10005000}/')
    assert r.status_code == 404


def test_update_role_detail_status_ok(test_client, test_role,
                                      test_privilege):
    r = test_client.put(f'/role/{test_role.id}/',
                        {f"name": "Some role",
                         "privileges": {test_privilege.id}})
    assert r.status_code == 200
    d = r.json()
    assert d.get('name') == 'Some role'


def test_update_role_detail_status_not_ok(test_client, test_privilege):
    r = test_client.put(f'/role/{10005000}/', {f"name": "Some role",
                                               "privileges": {test_privilege.id}})
    assert r.status_code == 404


def test_partial_update_role_detail_status_ok(test_client, test_role):
    r = test_client.patch(f'/role/{test_role.id}/', {f"name": "Some role partial"})
    assert r.status_code == 200
    d = r.json()
    assert d.get('name') == 'Some role partial'


def test_partial_update_role_detail_status_not_ok(test_client, test_role,
                                                  test_privilege):
    r = test_client.patch(f'/role/{10005000}/',
                          {f"name": "Some role partial",
                           "privileges": {test_privilege.id}})
    assert r.status_code == 404


def test_delete_role_detail_status_ok(test_client, test_role):
    r = test_client.delete(f'/role/{test_role.id}/')
    assert r.status_code == 204


def test_delete_role_detail_does_not_exist(test_client, test_role):
    r = test_client.delete(f'/role/{10005000}/')
    assert r.status_code == 404


'''Testing persons'''


def test_create_person_status_created(test_client, test_role, db):
    data = {
        'name': fake.name(),
        'password': fake.password(length=12),
        'email': fake.email(),
        'role': test_role.id
    }
    req = test_client.post('/person/', data)
    assert req.status_code == 201
    assert 'name' in data
    assert req.json() == req.json()


def test_create_person_status_bad_request(test_client, db):
    data = {}
    req = test_client.post('/person/', data)
    assert req.status_code == 400
    assert req.json() == {'name': ['This field is required.'],
                          'email': ['This field is required.'],
                          'role': ['This field is required.']}
    assert req.json() == req.json()


def test_view_persons_status_ok(test_client, test_person):
    r = test_client.get('/person/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_persons_status_not_found(test_client, test_person):
    with pytest.raises(ValueError):
        r = test_client.get('/persons/')
        assert r.status_code == 404
        assert r.json() == r.json()


def test_view_person_detail_status_ok(test_client, test_person):
    r = test_client.get(f'/person/{test_person.id}/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_person_detail_does_not_exist(test_client, test_person):
    r = test_client.get(f'/person/{10005000}/')
    assert r.status_code == 404


def test_update_person_detail_status_ok(test_client, test_person,
                                        test_role, test_privilege):
    r = test_client.put(f'/person/{test_person.id}/',
                        {f"name": {fake.name()},
                         "password": fake.password(length=12),
                         "email": {fake.email()},
                         "role": {test_role.id}})
    test_role.privileges.set({test_privilege})
    assert r.status_code == 200


def test_update_person_detail_status_not_ok(test_client, test_role):
    r = test_client.put(f'/person/{10005000}/',
                        {f"name": {fake.name()},
                         "password": fake.password(length=12),
                         "email": {fake.email()},
                         "role": {test_role.id}})
    assert r.status_code == 404


def test_partial_update_person_detail_status_ok(test_client, test_person,
                                                test_role, test_privilege):
    r = test_client.patch(f'/person/{test_person.id}/',
                          {f"email": {fake.email()}})
    test_role.privileges.set({test_privilege})
    assert r.status_code == 200


def test_partial_update_person_detail_status_not_ok(test_client,
                                                    test_role, test_privilege):
    r = test_client.patch(f'/person/{10005000}/',
                          {f"name": {fake.name()}})
    assert r.status_code == 404


def test_delete_person_detail_status_ok(test_client, test_person):
    r = test_client.delete(f'/person/{test_person.id}/')
    assert r.status_code == 204


def test_delete_person_detail_does_not_exist(test_client, test_person):
    r = test_client.delete(f'/person/{10005000}/')
    assert r.status_code == 404


'''Testing examples'''


def test_create_example_status_created(test_client, test_privilege,
                                       test_person, test_data, db):
    data = {
        'number_big': fake.bothify('%############'),
        'char': fake.word(),
        'email': fake.email(),
        'float': float(fake.bothify('%###.###')),
        'number': fake.random_digit(),
        'generic_ip_address': fake.ipv4(),
        'foreign': test_person.id,
        'many_to_many': test_privilege.id,
        'one_to_one': test_data.id,
        'time_n': fake.time(),
        'uu_id': fake.uuid4(),
        'json': fake.json(num_rows=1)
    }
    req = test_client.post('/example/', data)
    assert req.status_code == 201
    assert 'uu_id' in data
    assert req.json() == req.json()


def test_create_example_status_bad_request(test_client, db):
    data = {}
    req = test_client.post('/example/', data)
    assert req.status_code == 400
    assert req.json() == \
           {'number_big': ['This field is required.'],
            'char': ['This field is required.'],
            'email': ['This field is required.'],
            'float': ['This field is required.'],
            'number': ['This field is required.'],
            'generic_ip_address': ['This field is required.'],
            'time_n': ['This field is required.'],
            'uu_id': ['This field is required.'],
            'json': ['This field is required.'],
            'foreign': ['This field is required.'],
            'one_to_one': ['This field is required.']}
    assert req.json() == req.json()


def test_view_examples_status_ok(test_client, test_example):
    r = test_client.get('/example/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_examples_status_not_found(test_client, test_example):
    with pytest.raises(ValueError):
        r = test_client.get('/examples/')
        assert r.status_code == 404
        assert r.json() == r.json()


def test_view_example_detail_status_ok(test_client, test_example):
    r = test_client.get(f'/example/{test_example.auto}/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_example_detail_does_not_exist(test_client, test_example):
    r = test_client.get(f'/example/{10005000}/')
    assert r.status_code == 404


def test_update_example_detail_status_ok(test_client, test_person,
                                         test_privilege, test_example,
                                         test_data):
    r = test_client.put(
        f'/example/{test_example.auto}/',
        {f"number_big": {fake.bothify('%############')},
         "char": {fake.word()},
         "email": {fake.email()},
         "float": {float(fake.bothify('%#.#'))},
         "number": {fake.random_digit()},
         "generic_ip_address": {fake.ipv4()},
         "time_n": {fake.time()},
         "uu_id": {fake.uuid4()},
         "json": {fake.json()},
         "foreign": {test_person.id},
         "one_to_one": {test_data.id}})
    test_example.many_to_many.set({test_privilege})
    assert r.status_code == 200


def test_update_example_detail_status_not_ok(test_client,
                                             test_person, test_data):
    r = test_client.put(
        f'/example/{10005000}/',
        {f"number_big": {fake.bothify('%############')},
         "char": {fake.word()},
         "email": {fake.email()},
         "float": {float(fake.bothify('%#.#'))},
         "number": {fake.random_digit()},
         "generic_ip_address": {fake.ipv4()},
         "time_n": {fake.time()},
         "uu_id": {fake.uuid4()},
         "json": {fake.json()},
         "foreign": {test_person.id},
         "one_to_one": {test_data.id}})
    assert r.status_code == 404


def test_partial_update_example_detail_status_ok(test_client, test_person,
                                                 test_privilege, test_example):
    r = test_client.patch(
        f'/example/{test_example.auto}/',
        {f"email": {fake.email()},
         "float": {float(fake.bothify('%#.#'))},
         "generic_ip_address": {fake.ipv4()},
         "time_n": {fake.time()}})
    test_example.many_to_many.set({test_privilege})
    assert r.status_code == 200


def test_partial_update_example_detail_status_not_ok(
        test_client, test_person, test_data):
    r = test_client.patch(
        f'/example/{10005000}/',
        {f"number_big": {fake.bothify('%############')},
         "char": {fake.word()},
         "uu_id": {fake.uuid4()},
         "json": {fake.json()},
         "one_to_one": {test_data.id}})
    assert r.status_code == 404


def test_delete_example_detail_status_ok(test_client, test_example):
    r = test_client.delete(f'/example/{test_example.auto}/')
    assert r.status_code == 204


def test_delete_example_detail_does_not_exist(test_client, test_example):
    r = test_client.delete(f'/example/{10005000}/')
    assert r.status_code == 404


def test_get_boolean(mocker):
    mocker.patch('app.example.is_true', return_value=True)
    assert get_boolean() == 'True'


def test_get_data(mocker):
    mocker.patch('app.example.get_data', return_value={
        "id": 1000,
        "name": "abcdef"
    })


def test_requests_mock(requests_mock):
    requests_mock.get('http://testing_requests.com', text='data')
    assert 'data' == requests.get('http://testing_requests.com').text
