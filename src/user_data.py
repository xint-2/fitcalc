import sys, pickle
from classes import User
from calories import add_user_meal
from exercise import add_user_activity
from utils import clear

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
    clear()
    print("\nEnter Q at any prompt to exit.")

    try:
        with open('data.pickle', 'rb') as file:
            users = pickle.load(file)
    except (FileNotFoundError, EOFError):
        users = {}

    username = input("\nWhat is your name?: ")

    if username.upper() == "Q":
        clear()
        print("\nGoodbye!\n")
        sys.exit
    elif username not in users:
        clear()
        print("User not found. Creating a new one...\n")
        get_basic_stats()
    else:
        clear()
        home_page(username)
        return users[username]  # return the user for later use


def bmi_calc(weight, height): # for lbs
   if height is None or weight is None:
       raise ValueError("Weight and Height must be provided")
   return round(703 * (weight / (height ** 2)), 2)

def get_bmr(weight, height, gender, age):
    kg_weight = float(weight) * 0.45359237
    cm_height = float(height) * 2.54
    if gender.upper() == "M":
        bmr = ((10 * kg_weight) + (6.25 * cm_height)) - ((5 * age) + 5) # male bmr
    elif gender.upper() == "F":
        bmr = ((10 * kg_weight) + (6.25 * cm_height)) - ((5 * age) - 161) # female bmr
    else:
        bmr = ((10 * kg_weight) + (6.25 * cm_height)) - ((5 * age) - 161) # other use female
    
    return int(bmr)

def get_input(prompt, cast_type=str):
    value = input(prompt)
    if value.upper() == "Q":
        sys.exit("Exiting program.")
    try:
        return cast_type(value)
    except ValueError:
        print(f"invalid input. Expected a {cast_type.__name__}.")
        return get_input(prompt, cast_type)

def get_valid_age():
    while True:
        _age = get_input("Age: ", int)
        if _age <= 13:
            print("13 and younger to the pediatrics",)
        elif _age >= 99:
            print("99 and over, go see a doctor")
        else:
            return _age

def get_valid_gender():
    while True:
        _gender = get_input("Gender (M/F/O): ")
        if _gender.upper() in ["M", "F", "O"]:
            return _gender
        print("Invalid M, F or O")

def get_valid_weight():
    while True:
        _weight = get_input("Enter weight in lbs: ", int)
        if _weight > 999:
            print("Invalid Weight, higher than four digits")
        elif _weight <= 0:
            print("weight cannot be 0")
        else:
            return _weight

def get_valid_height():
    while True:
        _height = get_input("Enter height in inches: ", int)
        if _height > 108:
            print("Invalid height over 9 feet")
        elif _height < 36:
            print("Invalid height of 3 feet or less")
        else:
            return _height

def get_valid_goal():
    while True:
        _goal = get_input("Enter weight goal: ", int)
        if _goal > 999:
            print("Reach for the stars, land on the moon.")
        elif _goal <= 0:
            print("goal weight cannot be 0")
        else:
            return _goal

def home_page(username):
    clear()
    print(f"\nWelcome back, {username}!")
    while True:
        print("\nHome Page")
        print("----------------")
        print("0) View stats")
        print("1) Add Workout")
        print("2) Add Food")
        print("3) Edit Profile")
        print("4) View profiles on device")
        print("5) Delete profile")
        print("Q) Exit program")
        print("------------------\n")

        option = input("Choose option 1-4: ")
        if isinstance(option, str):
            option = option.upper()
    
        match option:
            case "0":
                print_stats(username)
            case "1":
                add_user_activity(username)
            case "2":
                add_user_meal(username)
            case "3":
                edit_profile(username)
            case "4":
                view_profiles()
            case "5":
                delete_profile(username)
            case ("Q"):
                clear()
                print("\nGoodbye!\n")
                sys.exit()
            case _:
                clear()
                print("\nInvalid. choose a value 0-4! or Q to quit")

def edit_profile(username):
    try:
        with open('data.pickle', 'rb') as file:
            users = pickle.load(file)
    except (FileNotFoundError, EOFError):
        print("No user data found.")
        return

    if username not in users:
        print(f" User '{username}' not found")
        return
    
    clear()

    while True:
        print("\n----------------")
        print("1) Back to Home")
        print("2) Edit Age")
        print("3) Edit Gender")
        print("4) Edit Weight")
        print("5) Edit Height")
        print("6) Edit Goal")
        print("----------------\n")

        option = input("What value would you like to edit? 2-6: ")

        match option:
            case "1":
                clear()
                break
            case "2":
                users[username].age = get_valid_age()
            case "3":
                users[username].gender = get_valid_gender()
            case "4":
                users[username].weight = get_valid_weight()
            case "5":
                users[username].height = get_valid_weight()
            case "6":
                users[username].goal = get_valid_goal()
            case _:
                clear()
                print("\nInvalid option choose 1-6!")
                break

        with open('data.pickle', 'wb') as file:
            pickle.dump(users, file)
        
        print(f"{username}'s profile updated.\n")
        


def delete_profile(username):
    clear()
    try:
        with open('data.pickle', 'rb') as file:
            users = pickle.load(file)
    except (FileNotFoundError, EOFError):
        print("No user data found.")
        return
    
    if username in users:

        print(f"\ndo you really want to delete your profile {username}? Y/N")

        y_n = input("Y/N?: ")

        if y_n.upper() == "Y":
            del users[username]
            with open("data.pickle", "wb") as file:
                pickle.dump(users, file)
            print("\nUser deleted.")
            clear()
            login()

        elif y_n.upper() == "N":
            return
        else:
            print("Invalid. Y/N")

def view_profiles():
    clear()
    print("Printing profiles")
    try:
        with open('data.pickle', 'rb') as file:
            users = pickle.load(file)
    except (FileNotFoundError, EOFError):
        print("No user data found.")
        return

    for name in users:
        print(f"Name: {name}")



def print_stats(username):
    clear()
    with open('data.pickle', 'rb') as file:
        users = pickle.load(file)

    if username not in users:
        print("User not found.")
        return

    user = users[username]
    bmi = bmi_calc(user.weight, user.height)
    bmr = get_bmr(user.weight, user.height, user.gender, user.age)

    print(f"\nStats for {user.name}:")
    print("----------------")
    print(f"User ID: {user.user_id}")
    print(f"Gender: {user.gender}")
    print(f"Age: {user.age}")
    print(f"Weight: {user.weight} lbs")
    print(f"Height: {user.height} inches")
    print(f"Weight Goal: {user.goal} lbs")
    print(f"{user.name}'s BMR: {bmr}")
    print(f"{user.name}'s BMI: {bmi}")
    print("----------------\n")
    if user.meals:
        print("Meals eaten:")
        for meal in user.meals:
            print(f"\n- {meal.meal_type}: {meal.meal_name} -> calories: ({meal.calories})")
    else:
        print("No meals logged yet.")

    print("\n----------------")

    if user.activities:
        print("Activities done: ")
        for activity in user.activities:
            print(f"\n - {activity.act_type}: {activity.act_name} -> calories burned: ({activity.burned_cal})")
    else:
        print("No activities logged")

    print("\n----------------")
    
    print(f"\nNet total calories: {user.calories_total}")


