# function (def) = A block of resuable code
#               place () after the function name to invoke(call) it

    # Calling the function is like pressing the button - Python immediately runs all the code saved under that name.



def msg():      # 'def' -> short for 'define'
    print("Welcome")
    print("HOME")
    print()

msg()   # -> invoking (calling) the func.
msg()
msg()   # we can call how many times we want



# 1. parameters and arguments


def happy_birthday(name, age):      # (name, age): These are called 'parameters'. Think of them as empty slots waiting to receive information when you press the button.
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("ravi", 20)      # The actual values passing inside, when calling the function are called 'arguments'.
happy_birthday("deepak", 23)



# ** Wrong one:**
# happy_birthday(50, "kim")  # arguments should be pass in crt order


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 2. return
    # instead of printing the stmts, You want it to do some math and hand the answer back to you, so you can save it or use it somewhere else.


def add(x, y):
    z=x+y
    return z

print(add(1, 2))    # **The function call add(1, 2) literally disappears and gets replaced by whatever value was returned!**



    # return -> working flow:
'''
print( add(1, 2) )
         │
         ▼
     1 + 2 = 3
         │
         └──► 'return 3' sends 3 back here
         │
print(   3   )  ──► Terminal displays: 3
'''





def name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = name("santhosh", "kumar")
print(full_name)









                # print                                        vs                          return

# 1. Displays text on the screen for the user                                  Sends a value back to the code
# **2. Can you store it in a variable? -> No (it becomes None)                 Yes (result = add(2, 3))
# 3. Status messages, menus, banners                                           Calculations, data processing
