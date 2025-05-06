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
    _bmi = bmi_calc(_weight, _height)

    user = User(_username, _weight, _height, _age, _gender, _bmi, _goal)
    users[_username] = user

    with open('data.pickle', 'wb') as file:
        pickle.dump(users, file)

    print("User saved successfully!")



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
        print("User not found. Creating a new one...")
        get_basic_stats()
    else:
        print(f"Welcome back, {username}!")
        print_stats(username)
        return users[username]  # return the user for later use
        



def print_stats(username):
    with open('data.pickle', 'rb') as file:
        users = pickle.load(file)

    if username not in users:
        print("User not found.")
        return

    user = users[username]
    bmr = get_bmr(user.weight, user.height, user.gender, user.age)

    print(f"\nStats for {user.name}:")
    print(f"Gender: {user.gender}")
    print(f"Age: {user.age}")
    print(f"Weight: {user.weight} lbs")
    print(f"Height: {user.height} inches")
    print(f"BMI: {user.bmi:.2f}")
    print(f"Weight Goal: {user.goal} lbs")
    print(f"{user.name}'s BMR: {bmr} \n")


