db = [{'id': 0, 'name': 'kathrin'}, {'id': 1, 'name': 'nenad'}]


def add_user(user):
    new_user = {'id': len(db), 'name': user['name']}
    db.append(new_user)
    return 200

def update_user(id, new_user): 
    current_user = [index for index, user in enumerate(db) if user['id'] == id]  
    current_user_index = current_user[0]
    db[current_user_index] = new_user
    return 200