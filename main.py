from config import URL
from pymongo import MongoClient
from functions import get_user
from functions import create_user
from functions import delete_user
from functions import update_user
from functions import default


if __name__ == '__main__':
    # Connect to the mongodb server, get the database and the collection
    client = MongoClient(URL)
    database = client['cursoMongoDB']
    collection = database['users']

    options = {
        "a": create_user,
        "b": get_user,
        "c": delete_user,
        "d": update_user
    }


    while True:
        for key, function in options.items():
            print(f"{key}.", function.__doc__)

        option = input("Select the letter for an option (q or quit to exit): ").lower()

        if option == "q" or option == "quit":
            break

        function_selected = options.get(option, default)
        function_selected(collection)