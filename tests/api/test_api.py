import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == 'Viktor'


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Sokol'



def test_remove_name(user):
    user.name = ''
    assert user.name == ''


def test_name(user):
    assert user.name == "Viktor"


def test_second_name(user):
    assert user.second_name == "Sokol"
