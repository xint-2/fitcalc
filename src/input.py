import sys

def bmi_calc(weight, height): # for lbs
   if height is None or weight is None:
       raise ValueError("Weight and Height must be provided")
   return 703 * (weight / (height ** 2))

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
