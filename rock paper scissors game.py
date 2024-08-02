import random

def play_game():
  user_score = 0
  computer_score = 0

  while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
      print("Invalid choice. Please enter rock, paper, or scissors.")
      user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
      print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
      print("You win!")
      user_score += 1
    else:
      print("Computer wins!")
      computer_score += 1

    print(f"\nScore:\nYou: {user_score}\nComputer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
      break

play_game()
