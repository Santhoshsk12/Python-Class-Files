import random

options = ["stone", "paper", "sissor"]
running = True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter you choice: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("It's a Tie.")
    elif player == "stone" and computer == "sissor":
        print("You Win!")
    elif player == "paper" and computer == "stone":
        print("You Win!")
    elif player == "sissor" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose.")


    if not input("Play again (y/n): ").lower() == "y":
        running = False


print("Thanks for Playing!")
    