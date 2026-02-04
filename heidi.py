from Chapter2.main import UserService
import pytest
from datetime import data

pytest.fixture(autouse=True)
def setup_sevice():

    service._db.clear()
    service._db.extend([{'id': 0, "name": 'Nenad'}])


def test_add_user():
    num_input = 1
    date_input = date(2026,1,31)
    list_input = [1,2,3]
    short_text_input_actual_number = '1'
    correct_text_input = 'new_user'
    service = UserService()

    setup_service(service)
    assert service.add_user(num_input) == {'id': 1, 'name':'new_user'}
    service.add_user(list_input) == {'id': 1, 'name': 'new_user'}
    service.add_user(date_input) == {'id': 1, 'name': 'new_user'}
    service.add_user(short_text_input_actual_number) == {'id': 1, 'name': 'new_user'}
    service.add_user(correct_text_input) == {'id': 1, 'name': 'new_user'}
