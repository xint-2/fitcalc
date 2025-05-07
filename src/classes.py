
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
        self.calories_total = 0

    def add_meal(self, food_obj):
        self.meals.append(food_obj)
        
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
        self.act_type = act_type
        self.burned_cal = burned_cal
        self.act_name = act_name
        self.activities = []
       
    def append_activty(self, act_name):
        self.activities.append(act_name)

    def burned_counter(self, burned_cal):
        self.burned_cal += burned_cal

