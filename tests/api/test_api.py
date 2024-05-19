


def test_remove_name(user):
    user.name = ''
    assert user.name == ''


def test_name(user):
    assert user.name == "Viktor"


def test_second_name(user):
    assert user.second_name == "Sokol"
