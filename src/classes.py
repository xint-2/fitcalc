
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

class Activity():
    pass

class Food():
    pass 