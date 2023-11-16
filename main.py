import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    #TIE
    if player == computer:
        print("Its a Tie!")

    #PLAYER WINNING
    if player == "Rock" and computer == "Scissors":
        print("Player WINS!")
    elif player == "Paper" and computer == "Rock":
        print("Player WINS!")
    elif player == "Scissors" and computer == "Paper":
        print("Player WINS!")

    #COMPUTER WINNING
    if player == "Rock" and computer == "Paper":
        print("Computer WINS!")
    elif player == "Paper" and computer == "Scissors":
        print("Computer WINS!")
    elif player == "Scissors" and computer == "Rock":
        print("Computer WINS!")

    a = input("Play Again? (y/n): ")
    if not a.lower() == "y":
        running = False

print("Thank You for Playing!")