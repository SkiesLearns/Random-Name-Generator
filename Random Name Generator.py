## Random Name Generator
import random

names = ['James', 'Michael', 'Paul', 'Mark', 'John', 'Adam', 'Curtis']
surnames = ['Baxter', 'Andrews', 'Coles', 'Collin', 'Adams', 'Smith', 'Doe']

def getName(names, surnames):
    while True:
        userResponse = input('\nPRESS ENTER TO GET A RANDOM NAME\n')
        f_name = random.choice(names)
        l_name = random.choice(surnames)
        print("""================================
NAME RANDOMISED
First Name: """+f_name+"""
Last Name: """+l_name+"""
================================""")

getName(names, surnames)
