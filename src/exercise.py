import pickle
from classes import Activity
from utils import clear

def add_exercise(activity_obj): # append exercise to exercise list
    clear()
    exercise = input("What exercise did you do?: ").strip()
    #exercise_type = input ("1) Anaerobic 2) Aerobic?: ")
    if not exercise:
        print("Invalid Exercise")
        return
    activity_obj.append_exercise(exercise)

def add_burned(activity_obj): # add calories to total burned calories
    clear()
    burned = int(input("Calories expended?: "))
    if not burned:
        print("Invalid Expendature")
        return
    activity_obj.burned_counter(burned)

def workout_menu():
    clear()
    name = input("What activity did you do?: ")
    type = input("Aerobic or Anerobic activity?: ")
    my_activity = Activity(type, 0, name)

    #if not name or type:
        #print("Invalid input. Discarding")
        #return None
    
    while True:
        print("\n--- Workout Menu ---")
        print("1) Add exercise to activity")
        print("2) View exercise list")
        print("3) Add calories expended")
        print("4) View calories expended")
        print("5) Discard and Exit")
        print("6) Save and Exit")
        print("---------------------\n")

        choice = input("Choose an Option 1-6: ")

        match choice:
            case "1":
                add_exercise(my_activity)
            case "2":
                clear()
                print("\nExercises done: ", my_activity.show_exercises())
            case "3":
                add_burned(my_activity)
            case "4":
                clear()
                print("\nShow burned calories: ", my_activity.show_burned_cal())
            case "5":
                clear()
                print("Discarded.")
                return None
            case "6":
                clear()
                return my_activity
            case _:
                clear()
                print("\nInvalid option choose again.")

def add_user_activity(username):
    try:
        with open('data.pickle', 'rb') as file: # open user file
            users = pickle.load(file)
    except (FileNotFoundError, EOFError):
        print("User not found.")
        return
    
    if username not in users:
        print("User not found.")
        return
    
    user = users[username]

    if not hasattr(user, 'activities'):
        user.activities = []

    activity_obj = workout_menu()

    if activity_obj is None:
        return
    
    user.add_activity(activity_obj)
    user.subtract_calories(activity_obj.burned_cal)

    with open('data.pickle', 'wb') as file:
        pickle.dump(users, file)
    
    print(f"{activity_obj.act_name} added to {username}'s workout log.")


