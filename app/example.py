from time import sleep


def is_true():
    sleep(5)
    return True


def get_boolean():
    return 'True' if is_true() else 'False'


def get_some_big_data():
    sleep(100)
    return {
        "id": 100,
        "name": "qwerty"
    }


def get_data():
    return get_some_big_data()
