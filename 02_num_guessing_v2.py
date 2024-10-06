# Project 02: Number Guessing Game version-2

import random 

number = random.randint(1, 100)

while True:
    try:
        guess = int(input('Guess the number between 1 - 100: '))
        
        if guess > number:
            print("Too High.")
        elif guess < number:
            print('Too Low.')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print("Please enter a valid number!")
