import pickle
from classes import Food
from utils import clear
from colorprint import *

# add food to Food instance food_obj.food_list[]
def add_food(food_obj):
    clear()
    print_cyan("Press Q to quit\n")
    meal = input("What food did you eat?: ").strip() # meal input str
    if not meal:
        print_red("Invalid food name")
        return
    if meal.upper() == "Q":
        return
    food_obj.append_food(meal) # append meal str to food_list 
    print(f"\n{meal} added to your food list.")
# add calories to food_obj.calories
def add_calories(food_obj):
    clear()
    print_cyan("Press Q to quit\n")
    amount = input("How many calories?: ")
    if not isinstance(amount, int):
        if str(amount).upper() == "Q":
            return
        else:
            clear()
            print_red("Only Integers.")
            return
    print(f"Calories added {amount}")
    food_obj.calorie_counter(amount)

# food menu -> add calories, food and view
def menu():
    clear()
    print_cyan("Enter Q return home\n")

    meal_type = input("Enter meal type (e.g., Breakfast, Lunch): ")
    if meal_type.upper() == "Q":
        return
    
    meal_name = input("Enter initial meal name: ")
    if meal_name.upper() == "Q":
        return

    my_food = Food(meal_type, 0, meal_name) # new Food class instance

    if not meal_type or not meal_name:
        print_red("Invalid Input. Discarding")
        return None

    while True:
        print_cyan("\n--- Meal Menu ---")
        print("1. Add a food item")
        print("2. View food list")
        print("3. Add calories")
        print("4. View total calories")
        print("5. Exit And discard meal")
        print("6. Save and return to home")
        print_cyan("-----------------")

        choice = input("\nChoose an option 1-6: ")

        match choice:
            case "1":
                add_food(my_food)
            case "2":
                clear()
                print("\nFoods eaten:", my_food.show_foods())
            case "3":
                add_calories(my_food)
            case "4":
                clear()
                print("\nTotal calories:", my_food.show_calories())
            case "5":
                clear()
                print_red("\nDiscarded.")
                return None
            case "6":
                clear()
                print_green("\nSaved")
                return my_food
            case _:
                clear()
                print("\nInvalid option. Please choose again.")

# adds food_obj to the users data
def add_user_meal(username):
    try:
        with open('data.pickle', 'rb') as file: # open user file
            users = pickle.load(file)
    except (FileNotFoundError, EOFError):
        print_red("User not found.")
        return
    
    if username not in users:
        print_red("User not found.")
        return
    
    user = users[username]

    if not hasattr(user, 'meals'):
        user.meals = []
    
    food_obj = menu()

    if food_obj is None:
        return

    user.add_calories(food_obj.calories)
    user.add_meal(food_obj)

    with open('data.pickle', 'wb') as file:
        pickle.dump(users, file)
    
    print(f"{food_obj.meal_name} added to {username}'s meal log.")
