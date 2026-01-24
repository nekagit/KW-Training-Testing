import pytest
from main import db, add_user, update_user, delete_user, list_db

# This fixture resets the database before every single test function
@pytest.fixture(autouse=True)
def setup_db():
    db.clear()
    db.extend([{'id': 0, 'name': 'kathrin'}, {'id': 1, 'name': 'nenad'}])

def test_add_user():
    new_user = {'name': 'stefan'}
    status = add_user(new_user)
    
    assert status == 200
    assert len(db) == 3
    assert db[2]['name'] == 'stefan'
    assert db[2]['id'] == 2

def test_update_user():
    updated_data = {'id': 1, 'name': 'nenad_updated'}
    status = update_user(1, updated_data)
    
    assert status == 200
    assert db[1]['name'] == 'nenad_updated'

def test_delete_user():
    # Initial length is 2
    status = delete_user(0)
    
    assert status == 200
    assert len(db) == 1
    assert db[0]['name'] == 'nenad'  # Only nenad should remain

def test_list_db(capsys):
    status = list_db()
    # capsys captures the print statements
    captured = capsys.readouterr()
    
    assert status == 200
    assert "kathrin" in captured.out
    assert "nenad" in captured.out

def test_delete_non_existent_user_raises_error():
    # This test demonstrates that your current code crashes 
    # if an ID doesn't exist.
    with pytest.raises(IndexError):
        delete_user(999)