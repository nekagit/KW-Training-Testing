import pytest
from main import db, add_user, update_user, delete_user, list_db

@pytest.fixture(autouse=True)
def setup_db():
    db.clear()
    db.extend([{'id': 0, 'name': 'Nalan'}, {'id':1, 'name': 'Nenad'}])

def test_add_user():
    new_user = {'name': 'Stefan'}
    status = add_user