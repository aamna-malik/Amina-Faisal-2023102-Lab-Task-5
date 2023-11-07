import random

choices = ['rock', 'paper', 'scissors']

while True:
    print("Enter your choice: rock, paper, or scissors. To exit the game, type 'exit'")
    player_choice = input().lower()
    if player_choice == 'exit':
        break
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
