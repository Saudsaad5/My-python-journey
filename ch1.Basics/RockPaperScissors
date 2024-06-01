import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
    
    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")

    elif player == "rock" and computer == "scissors":
        print("You win!")
    
    elif player == "paper" and computer == "rock":
        print("You win!")

    elif player == "scissors" and computer == "paper":
        print("You win!")

    else:
        print("You lose!")
    print("--------------------")

    if not input("Do you want to try again? (y/n): ").lower() == "y":
        print("--------------------")
        print("Thank you for palying!")
        running = False
    print("--------------------")
    