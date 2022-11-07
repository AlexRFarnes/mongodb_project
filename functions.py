import os 

import pprint

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

    address = input('Do you want to enter your address? (y/n) ').lower()

    if address == 'y':
       user['address'] = get_address()

    collection.insert_one(user)

    show_user(user)

    return user

def get_address():
    street = input("Street: ")
    district = input("District: ")
    city = input("City: ")
    zip_code = input("Zip code: ")

    address = dict(street=street, district=district, city=city, zip_code=zip_code)
    return address


def show_user(user):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(user)

@clear_system
def get_user(collection):
    """Get an user's info"""
    
    username = input('Username: ')
    user = collection.find_one(
        {'username': username},
        {'_id': False}
    )

    if user:
        show_user(user)
        return user
    else:
        print("It was not possible to get that user.")


@clear_system
def delete_user(collection):
    """Delete an user"""

    username = input('Username: ')
    
    result = collection.delete_one({
        'username': username
    })
    print(result.acknowledged)

    return result.acknowledged


@clear_system
def update_user(collection):
    """Update an user"""
    print('Update user')


def default(*args, **kwargs):
    print("Not a valid option")