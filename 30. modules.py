# modules = A module is simply a file containing Python code (functions, variables, or classes) that you can include in your program.


# Think of a module like an extension pack or a toolbox:
    # Instead of writing thousands of lines of code into a 'single file', you separate code into 'different files'.
    # Python already comes with many pre-built toolboxes (like math, random, datetime).
    # You can also create your own custom toolboxes!



    # --- Exploring Built-in Modules ---
# You can see all available built-in modules in Python by typing:

# print(help("modules"))  # lists all installed modules


# To see what is inside a specific module:
import math

print(dir(math)) # lists all functions and constants inside 'math'


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Three Ways to Import a Module:

    # 1. Standard Import (import module_name)
            # can access everything by prefixing it with the module name:

import math

print(math.pi)
print(math.e)

    # 2. Aliasing (import module_name as alias)
            # Give the module a shorter nickname:

import math as m

print(m.pi)
print(m.e)

    # 3. Specific Import (from module_name import item)
            # Brings specific tools directly into your file so you don't need to type the module prefix:

from math import pi, e, sqrt


print(pi)
print(e)
print(sqrt(9))

print()

            # Warning: You can write from math import * (import everything),
            #           It clutters your workspace and can cause name conflicts 
            #           if you name a variable or function the same as something inside the module.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    # --- Creating Your Own Custom Module ---

# We will create two separate Python files in the same directory:

'''
my_project/
│
├── example.py   (Our custom toolbox)
└── main/modules.py      (Our program running the code)
'''


# after created our own python file -> example.py

# import 'example' just like a built-in module:


import example


res = example.pi
print(res)

res = example.square(3)
print(res)

res = example.cube(3)
print(res)

result = example.circumference(2)
print(result)
# print(f"Cirumference = {result:.2f}")

result = example.area(2)
print(result)
# print(f"Area = {res:.2f}")



# Visualize:
'''
main/modules.py                                   example.py
┌───────────────────────────┐               ┌───────────────────────────┐
│ import example            │ ────────────► │ pi = 3.14159              │
│                           │               │                           │
│ example.square(3)         │ ────────────► │ def square(x):            │
│       ▲                   │               │     return x ** 2         │
│       │                   │               │                           │
│ (Hands back 9)            │ ◄──────────── │                           │
└───────────────────────────┘               └───────────────────────────┘
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        # **** Important ****
''' 
        Syntax                                 How it works                                    Example
1. import module                  Imports module; access via dot notation                    math.sqrt(16)
2. import module as alias         Shortens module name for convenience                       m.sqrt(16) 
3. from module import item        Imports specific item directly                             sqrt(16) 
4. Custom Module                  Save code in a .py file, import by file name               import example
'''