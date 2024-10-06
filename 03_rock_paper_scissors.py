# Project 03: Rock, Paper, Scissors Game

import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = { ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️' }
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, or Scissors ? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid Choice!')


def display_choices(u_choice, c_choice):
    print(f'You chose {emojis[u_choice]}')
    print(f'Computer chose {emojis[c_choice]}')


def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Draw 🟰")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)
        ):
        print('👦 You win')
    else:
        print('💻 Computer win')


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        
        check_winner(user_choice, computer_choice)
        
        should_continued = input('Continue? (y/n): ').lower()
        if should_continued != 'y':
            break

play_game()