"""

Tests developed with pytest for api
"""
from src.part2_automation.t6_api_testing.my_api.learning_api_test_wrapper import call_get_method


def test_get_status_code():
    x = call_get_method()
    assert x[1] == 200


def test_get_content_is_dict():
    x = call_get_method()
    assert type(x[0]) is dict


def test_email_in_content():
    x = call_get_method()
    assert 'email' in x[0]['users'][0].keys()


def test_post():
    pass


def test_delete():
    pass


def test_put():
    pass

# pytest --html=apitest.html test_learning_api.py