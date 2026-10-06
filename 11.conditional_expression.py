# conditional expression = conditional expression (also called ternary operator) 
#                           is a way to make a decision in your code and choose a value in just one single line.
# Think of it as a shortcut for if-else statement. 
#           Instead of writing four lines of code to decide what value a variable should get, you can do it in one clear line.


# Syntax:

'''   value_if_true if condition else value_if_false    '''

# Python reads this in a unique order:
# 1. It looks at the condition in the middle first.
# 2. If that condition is True, it picks the value on the left (value_if_true).
# 3. If that condition is False, it picks the value on the right (value_if_false).



num = 20
result = "Even" if num%2 == 0 else "Odd"
print(result)


is_member = True
res = "Discount" if is_member else "No Discount"
print(res)

# using conditional expression inside the print function
online = True
print("Online" if online else "Offline")


print(100 if 5==5 else 200) # don't use quotes ("") because it is no's, not a string
#                                   if we use quotes ("") then math calculate will not work 





# if, elif, else -> in single line

# Nested Conditional Expressions (3+ Choices)
#               When you have more than two options, you can place a second conditional expression inside the else slot of the first one.


# Syntax:
'''  result = value_1 if condition_1 else (value_2 if condition_2 else value_3)   ''' # parenthesis are optional

# 1. Regular way -> if, elif, else 
light = "yellow"

if light == "red":
    action = "Stop"
elif light == "yellow":
    action = "Slow down"
else:
    action = "Go"


# 2. Nested one-line way
light = "yellow"

print("stop" if light == "red" else ("slow down" if light == "yellow" else "Go"))  # slow down





# Example 1:
score = 80
print(f"You { 'Passed' if score >= 50 else 'Failed' } the test.")


# Example 2:
count = 0

print(f"Status: {'Active' if count > 0 else 'Inactive'}  (Total: {count * 2})")
#                                               Output -> Status: Inactive (Total: 0)




            #  conditional logic in comprehension -> Important
# When you look at a Python list comprehension, 
# Python actually reads the end of the line first to figure out which numbers it is allowed to use.
# If there is an 'if statement' at the very end, it acts as a security guard (a filter). 
# If a number doesn't pass the guard, it gets thrown away immediately and never gets processed.

print([x for x in range(4) if x != 2])  # first look at if-stmt
    # [0, 1, 3]



print([x + 1 if x % 2 == 0 else x - 1 for x in range(4) if x != 2])

# The Filter Zone (At the back): for x in range(4) if x != 2 -> This selects our numbers. As we just saw, our valid numbers are 0, 1, and 3.
# The Decision Zone (At the front): x + 1 if x % 2 == 0 else x - 1 -> This transforms each valid number.

'''  Explanation:  '''
    # Step 1: Process x = 0
# Python runs the decision: 0 + 1 if 0 % 2 == 0 else 0 - 1
# Check condition: Is 0 % 2 == 0? (Is 0 an even number?) Yes (True).
# Pick value: Because it is True, Python does the math on the left: 0 + 1 = 1.
# Current List: [1]

    # Step 2: Process x = 1
# Python runs the decision: 1 + 1 if 1 % 2 == 0 else 1 - 1
# Check condition: Is 1 % 2 == 0? (Is 1 an even number?) No (False).
# Pick value: Because it is False, Python jumps to the right after the else: 1 - 1 = 0.
# Current List: [1, 0]

    # Step 3: Process x = 2
# Check filter: The guard at the back sees x != 2. Since 2 != 2 is False, 2 is completely skipped. No math is done.

    # Step 4: Process x = 3
# Python runs the decision: 3 + 1 if 3 % 2 == 0 else 3 - 1
# Check condition: Is 3 % 2 == 0? (Is 3 an even number?) No (False).
# Pick value: Because it is False, Python jumps to the right after the else: 3 - 1 = 2.
# Final List: [1, 0, 2]

'''   Output: [1, 0, 2]   '''