
import random

class User():
    def __init__(self, name, weight, height, age, gender, goal):
        self.user_id = random.randint(1, 1000)
        self.name = name 
        self.weight = weight
        self.gender = gender
        self.age = age
        self.height = height
        self.goal = goal
        self.meals = []
        self.activities = []
        self.calories_total = 0

    def add_meal(self, food_obj):
        self.meals.append(food_obj)

    def add_calories(self, calorie_count):
        self.calories_total += calorie_count

    def add_activity(self, activity_obj):
        self.activities.append(activity_obj)

    def subtract_calories(self, burned_calories):
        self.calories_total -= burned_calories
        
    def get_meal(self):
        return self.eaten
    
    

class Food():
    def __init__(self, meal_type, calories, meal_name):
        self.meal_type = meal_type
        self.calories = calories
        self.meal_name = meal_name
        self.food_list = []
        
    def calorie_counter(self, cal_number):
        self.calories += cal_number

    def append_food(self, food_name):
        self.food_list.append(food_name)

    def show_foods(self):
        return self.food_list
    
    def show_calories(self):
        return self.calories

class Activity():
    def __init__(self, act_type, burned_cal, act_name):
        self.act_name = act_name
        self.act_type = act_type
        self.burned_cal = burned_cal
        self.exercise_list = []
       
    def append_exercise(self, act_name):
        self.exercise_list.append(act_name)

    def show_exercises(self):
        return self.exercise_list

    def burned_counter(self, burned_cal):
        self.burned_cal += burned_cal

    def show_burned_cal(self):
        return self.burned_cal

