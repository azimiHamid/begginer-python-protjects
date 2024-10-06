# Project 02: Number Guessing Game

import random

number = random.randint(1, 100)

while True:
    user_guess = input('Guess the number between 1 - 100: ')
    
    if not user_guess.isdigit():
        print('Please enter a valid number')
        continue
    
    user_guess = int(user_guess)

    if user_guess < 1 or user_guess > 100:
        print('Please enter a number between 1 and 100.')
        continue
    
    if user_guess == number:
        print('Congratulations! You guessed the number.')
        break
    elif user_guess > number:
        print('Too High.')
    elif user_guess < number:
        print('Too Low')
