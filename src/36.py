import random

def game():
    choices = ["rock", "paper", "scissors"]
    player = input("Player's choice: ").lower()
    
    if player not in choices:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")

game()
