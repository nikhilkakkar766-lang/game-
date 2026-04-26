# main.py
from game_functions import play_sps, play_dice

while True:
    print("\n--- GAME MENU ---")
    print("1. Stone Paper Scissors")
    print("2. Dice Roll Game")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        play_sps()

    elif choice == "2":
        play_dice()

    elif choice == "3":
        print("Thanks for playing! 👋")
        break

    else:
        print("Invalid choice")