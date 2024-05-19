import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Viktor'

@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == 'Sokol'


# def test_change_name(user):
#     assert user.name == 'Viktor'


# def test_change_second_name(user):
#     assert user.second_name == 'Sokol'
