import random

def get_computer_choice():
    choice = random.randint(1, 3)
    if choice == 1:
        return "stone"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"

def get_player_choice():
    while True:
        try:
            choice = int(input("Enter 1 for stone, 2 for paper, and 3 for scissors: "))
            if choice == 1:
                return "stone"
            elif choice == 2:
                return "paper"
            elif choice == 3:
                return "scissors"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "stone" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "stone") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins!"
    else:
        return "Computer wins!"

while True:
    print(f"\n********Stone paper scissors game********\n")
    computer_choice = get_computer_choice()
    player_choice = get_player_choice()
    
    print(f"Computer chose: {computer_choice}")
    print(f"Player chose: {player_choice}")
    print(determine_winner(player_choice, computer_choice))
    
    response = input("Do you want to continue the game (enter y for yes and n for no): ").lower()
    if response == 'n':
        print("\n********Thanks for playing!********")
        break
