# List comprehension = A list comprehension is a concise way to create a new list in Python. 
#                       It allows you to take an existing iterable, process its items, and produce a brand new list in a single line of code.

    # compact and easier to read than traditional loops.
    # formula -> *** [expression 'for' value/item 'in' iterable 'if' condition] ***



# basic eg, squaring numbers
    # Traditional for loops:

double = []
for x in range(1, 11):
    double.append(x * 2)    #-> squaring the no's in each iteration
print(double)               # o/p: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


    # formula:
''' [expression 'for' item 'in' iterable] '''


    # list comprehension way:
double = [x * 2 for x in range(1, 11)]
print(double)


# Visualize:
'''
doubles = [  x * 2       for x in range(1, 11)  ]
               ▲                     │
               │                     ▼
               │              Loop runs: x = 1, 2, 3...
               │                     │
               └─────────────────────┘
         Calculate (x * 2) and append directly into the list!
'''



# Eg's:

triples = [y * 3 for y in range(1, 11)]
print(triples)
        # o/p: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


squares = [z * z for z in range(1, 11)]
print(squares)
        # o/p: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    # Working with strings

fruits = ["apple", "banana", "orange", "grapes"]

fruits = [fruit.upper() for fruit in fruits]
print(fruits)           # o/p: ['APPLE', 'BANANA', 'ORANGE', 'GRAPES']


    # instead we can do like this also


fruits = [fruit.upper() for fruit in ["apple", "banana", "orange", "grapes"]]
print(fruits)           # 0/p: ['APPLE', 'BANANA', 'ORANGE', 'GRAPES']



# Example: Grabbing just the first character of each string

fruits = ["apple", "banana", "orange", "grapes"]

fruits = [fruit[0] for fruit in fruits]
print(fruits)           # o/p: ['a', 'b', 'o', 'g']  -> first character of each iterables


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    # formula -> *** [expression 'for' value/item 'in' iterable 'if' condition] ***
        # with using 'if' condition

numbers = [1, -2, 3, -4, 5, -6, 7, -8]

positive_numbers = [num for num in numbers if num >= 0]
print(positive_numbers)     # [1, 3, 5, 7]

negative_numbers = [num for num in numbers if num < 0]
print(negative_numbers)     # [-2, -4, -6, -8]

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)         # [-2, -4, -6, -8]

odd_numbers = [num for num in numbers if num % 2 == 1]
print(odd_numbers)          # [1, 3, 5, 7]


# visualize:
'''
             ┌─────────── What to do to each item (Expression)
             │
             ▼
new_list = [ x * 2   for x in numbers   if x > 0 ]
                           ▲               ▲
                           │               │
From this source (Iterable)┘               └─ Only include if this is True (Filter) -> if condition
'''


# another eg:

grades = [85, 42, 79, 90, 35, 61, 20]

pass_grades = [grade for grade in grades if grade >= 40]
print(pass_grades)
                # o/p: [85, 42, 79, 90, 61]