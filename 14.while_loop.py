# while loop = while loop is used to repeatedly execute a block of code as long as a specified condition remains True.
#               codes executes/runs until the condition became False.

#         -----> if statement that checks a condition once, a while loop checks the condition, runs the code block, 
#                and then circles back to check the condition again. It only stops when the condition evaluates to False.



# name = input("Enter Name: ")

# while name == "":
#     print("You didn't entered your name")
#     name = input("Enter Name: ")
# print(name)



# age = int(input("Enter Age: "))

# while age < 18:
#     print("You are under age")
#     age = int(input("Enter Age: "))
# print(f"You are {age} years old")




# food = input("Enter the food (q to quit): ")

# while not food == 'q':
#     print(f"Food is: {food}")
#     food = input("Enter another food (q to quit): ")
# print("Bye")



# num = int(input("Enter no betwee 1-10: "))

# while num < 0 or num > 10:
#     print("no is NOT valid")
#     num = int(input("Enter no betwee 1-10: "))
# print(f"The no is: {num}")



# count = 3

# while count > 0:
#     print(count)
#     count -= 1  # Decrements count by 1 each iteration
# print("Blast")



# WARNING: This loop will never stop because 'x' is always 5
'''x = 5
while x == 5:
    print("Stuck in a loop!") '''

        # Tip: If your program gets stuck in an infinite loop in your terminal, press Ctrl + C to force it to stop.



                                    # break and continue

#  --> break and continue are control flow keywords used to alter the natural behavior of loops (for and while). 
#       They let you interrupt a loop based on a specific condition.

# break means "STOP immediately": It completely destroys the loop and exits it early.
# continue means "SKIP this one": It stops the current iteration and jumps straight back to the top of the(while/for) loop to check the condition again.It completely ignores any code written below it.
#                               -> Skips the rest of the current iteration and jumps straight back to the top to re-evaluate the condition.It completely ignores any code written below it.


# 1. break (Stop and Leave)
#       ==> counting from 1 to 5, when 3 comes stop and leave everything.

'''num = 1

while num <= 5:
    if num == 3:
        print("Quit")
        break
    print(num)
    num += 1 '''


# 2. continue (Skip and Keep Going)
#       --> in continue we need to give the counter variable before continue, otherwise we'll stuck into infinite loop.

''' num = 0

while num < 5:
    num += 1 # given the counter before the continue

    if num == 3:
        print("Skipped no", num)
        continue

    print(num) '''



        # What happens if we leave adding part at the bottom?
# Remember, continue stops the current turn and jumps straight back to the top of the loop. 
# ****It completely ignores any code written below it.****
# If we left the adding part at the bottom, look at what goes wrong:

# ❌ DANGER: This creates a broken, infinite loop!
''' num = 1

while num <= 5:
    if num == 3:
        print("Skip!")
        continue  # Jumps to the top! The code below is ignored!
        
    print(num)
    num = num + 1  # 😮 This line never runs when num is 3! '''


# The Trap:
# 1. num becomes 3.
# 2. Python enters the if statement and hits continue.
# 3. ****Python jumps back to the top while num <= 5 check.****
# 4. Since the adding line at the bottom was skipped, num is still 3.
# 5. Python checks num == 3 again, hits continue again, and gets stuck forever printing "Skip!".

#  so use this method
num = 0

while num < 5:
    num += 1 # given the counter before the continue

    if num == 3:
        print("Skipped no", num)
        continue

    print(num)


print("\n")
    # or (use this method)


num = 1 

while num <= 5:
    if num == 3:
        # num += 1 # we can give, here also
        print("Skipped")
        num += 1 # Fixes the issue by increasing it BEFORE skipping
        continue

    print(num)
    num += 1 # Standard increase for normal numbers

print("\n")




        # in while-loop using 'else'

# Syntax:
'''
while condition:
    code goes here
else:
    code goes here 
'''


# Eg:
count = 1
while count < 5:
    print(count)
    count += 1
else:
    print(count)

print("\n")


