import random


lowest_num = 1
highest_num = 50

answer = random.randint(lowest_num, highest_num)
guesses = 0



print("----- Number Guessing Game -----")
print(f"Enter a Number btw {lowest_num} and {highest_num}")
print()


while True:
    guess = (input("Enter your guess: "))

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Out of range!")
            print(f"Please select a number btw {lowest_num} and {highest_num}")
        elif guess < answer:
            print("guess is too low. Try again")
            print("---------------")
        elif guess > answer:
            print("guess is too high. Try again")
            print("---------------")
        else:
            print("**************")
            print(f"Correct! The answer is -> {answer}")
            print(f"The number of guesses -> {guesses}")
            print("**************")
            break


    else:
        print("Invalid!")
        print(f"Please select a number btw {lowest_num} and {highest_num}")
