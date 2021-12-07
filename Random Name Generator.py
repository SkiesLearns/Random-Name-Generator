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
        repeat = input('\nRANDOMISE ANOTHER NAME? (YES/NO)\n')
        if repeat.lower() == 'yes':
            getName(names, surnames)
        else:
            print('\nAPPLICATION CLOSED')
            exit()

getName(names, surnames)
