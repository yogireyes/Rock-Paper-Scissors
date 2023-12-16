import random

def play_rock_paper_scissors():
    actions = ["Rock", "Paper", "Scissors"]

    while True:
        # Computer makes a random choice
        computer_choice = random.choice(actions)

        # Player input
        player_choice = input("Choose Rock, Paper or Scissors (or type 'I quit' to end the game): ").capitalize()
        if player_choice == "I quit":
            print("Thank you for playing")
            break

        if player_choice not in actions:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        # Determine the winner and display the result
        print(f"Player: {player_choice}, Computer: {computer_choice}", end=", ")
        if player_choice == computer_choice:
            print("Result: Game Tied")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Scissors" and computer_choice == "Paper") or \
             (player_choice == "Paper" and computer_choice == "Rock"):
            print("Result: You win!")
        else:
            print("Result: You lose")

# Run the game
play_rock_paper_scissors()
