import pickle
from classes import *
from input import *


def get_basic_stats():
    try:
        with open('data.pickle', 'rb') as file:
            users = pickle.load(file)
    except (FileNotFoundError, EOFError):
        users = {}

    _username = get_input("Enter name: ")

    if _username in users:
        print("User already exists.")
        return

    _age = get_valid_age()
    _gender = get_valid_gender()
    _weight = get_valid_weight()
    _height = get_valid_height()
    _goal = get_valid_goal()
    
    user = User(_username, _weight, _height, _age, _gender, _goal)
    users[_username] = user

    with open('data.pickle', 'wb') as file:
        pickle.dump(users, file)

    print("User saved successfully!")
    home_page(_username)



def login():
    print("Enter Q at any prompt to exit.")

    try:
        with open('data.pickle', 'rb') as file:
            users = pickle.load(file)
    except (FileNotFoundError, EOFError):
        users = {}

    username = input("What is your name?: ")

    if username == "Q":
        sys.exit
    elif username not in users:
        print("User not found. Creating a new one...\n")
        get_basic_stats()
    else:
        print(f"\nWelcome back, {username}!")
        home_page(username)
        return users[username]  # return the user for later use
        


