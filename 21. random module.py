import random

    # for numbers that is (int) -> randint
'''num = random.randint(1, 6)      # random numbers from 1 to 6
print(num)


lowest = 1
highest = 10
number = random.randint(lowest, highest)
print(number)'''


    # for floating point numbers(float) -> random()
'''float_numbers = random.random()
print(float_numbers)'''        # o/p: 0.897446745256731


    # choice()
'''game = ("stone", "paper", "sissor")

guess = random.choice(game)
print(guess) '''           #o/p: randomly gives -> stone , or paper, or sissor


    # shuffle()
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J", "A"]

random.shuffle(cards)
print(cards)            # o/p: ['Q', '8', 'K', 'J', '2', '10', '9', '6', '3', 'A', '7', '5', '4']
