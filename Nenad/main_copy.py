db = [{'id': 0, 'name': 'Nalan'}, {'id':1, 'name': 'nenad'}]

def add_user(user):
    new_user = {'id': len(db), 'name': user['name']}
    db.append(new_user)
    return 200

def update_user(id, new_user):
    current_user = [index for index, user in enumerate(db) if user['id'] == id]
    current_user_index = current_user[0]
    db[current_user_index] = new_user
    return 200

def delete_user(id):
    user_to_del = [user for user in db if user['id'] == id]
    db.remove(user_to_del[0])
    return 200

def list_db():
    for user in db:
        print(user)
    return 200

if __name__ == '__main__':
    test_user = {'name': 'test'}
    add_user(test_user)
    test_user = {'id': 1, 'name': 'test2'}
    update_user(1, test_user)
    delete_user(2)
    list_db()