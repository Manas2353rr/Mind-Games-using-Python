import random

def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_wins = 0
    computer_wins = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()

        if player_choice == 'q':
            break
        elif player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose {player_choice}, computer chose {computer_choice}.")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            player_wins += 1
        else:
            print("You lose!")
            computer_wins += 1

        print(f"Score: You - {player_wins}, Computer - {computer_wins}\n")

    print(f"Final Score: You - {player_wins}, Computer - {computer_wins}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_rock_paper_scissors()
