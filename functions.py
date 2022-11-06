import os 

def clear_system(function):
    
    def wrap(*args, **kwargs):
        os.system('clear')
        result = function(*args, **kwargs)
        input('')
        os.system('clear')

    wrap.__doc__ = function.__doc__
    return wrap

@clear_system
def create_user(collection):
    """Create a new user"""
    
    username = input('Username: ')
    age = int(input('Age: '))
    email = input('Email: ')

    user = dict(username=username, age=age, email=email)
    collection.insert_one(user)

    print(user)

    return user

@clear_system
def get_user(collection):
    """Get an user's info"""
    
    username = input('Username: ')
    user = collection.find_one(
        {'username': username},
        {'_id': False}
    )

    print(user)

    return user

def delete_user():
    """Delete an user"""
    print('Delete user')

def update_user():
    """Update an user"""
    print('Update user')

def default(*args, **kwargs):
    print("Not a valid option")