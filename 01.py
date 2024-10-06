# Project 01: Dice Rolling Game

import random

def rollTheDice():
    nums = [1,2,3,4,5,6]
    x = random.choice(nums)
    y = random.choice(nums)
    print(f'({x}, {y})')


def checkUserChoice():
    while True:
        choice = input('Roll the dice? (y/n) ').lower() 
        if choice == 'y':
            rollTheDice()
        elif choice == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")


checkUserChoice()