import pytest
from pytest_mock import mocker
from rest_framework.test import APIClient
from app.factories import PrivilegeFactory, RoleFactory, PersonFactory, DataFactory, ExampleFactory


@pytest.fixture
def test_privilege(db):
    return PrivilegeFactory()


@pytest.fixture
def test_role(db):
    return RoleFactory()


@pytest.fixture
def test_person(db):
    return PersonFactory()


@pytest.fixture
def test_data(db):
    return DataFactory()


@pytest.fixture
def test_example(db):
    return ExampleFactory()


@pytest.fixture()
def test_client():
    return APIClient()


# @pytest.fixture()
# def mock_privilege_ok():
#     result = mocker.patch()
#     result.return_value = {
#
#     }
#     return result


