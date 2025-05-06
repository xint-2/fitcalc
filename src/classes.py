
import random

class User():
    def __init__(self, name, weight, height, age, gender, bmi, goal):
        self.user_id = random.randint(1, 1000)
        self.name = name 
        self.weight = weight
        self.gender = gender
        self.age = age
        self.height = height
        self.bmi = bmi
        self.goal = goal
