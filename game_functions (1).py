# game_functions.py

import random
from game_data import data

# Stone Paper Scissors Game
def play_sps():
    user = input("Enter stone / paper / scissors: ").lower()
    computer = random.choice(data["choice"])

    print("Computer chose:", computer)

    if user == computer:
        print("Draw!")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
    else:
        print("Computer Wins!")


# Dice Roll Game
def play_dice():
    user_roll = random.choice(data["dice_range"])
    comp_roll = random.choice(data["dice_range"])

    print("You rolled:", user_roll)
    print("Computer rolled:", comp_roll)

    if user_roll > comp_roll:
        print("You Win!")
    elif user_roll < comp_roll:
        print("Computer Wins!")
    else:
        print("It's a Draw!")