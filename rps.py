



# Function for computer to chose from a list of strings
import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    while player_choice not in choices:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        player_choice = input("Enter your choice: ").lower()
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    play_rps()