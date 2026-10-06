# if = Do some code only IF some condition is True
#       Else something else
#    --> one condition that is True, it executes that specific block of code and skips the entire rest of the structure. 


    # Syntax

'''
if condition1:
    # Executes if condition1 is True
    statement(s)
elif condition2:
    # Executes if condition1 is False AND condition2 is True
    statement(s)
else:
    # Executes if all previous conditions are False
    statement(s) 
'''


age = int(input("Enter Age: "))

if age < 0:
    print("Enter valid age.")
elif age >= 18:            # ------> elseif = elif
    print("You are Eligible.")
else:
    print("You are NOT Eligible.")


response = input("Do you like food (Y/N): ")

if response == 'Y':
    print("Have some food.")
else:
    print("Thank You!")


is_sale = True

if is_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")
