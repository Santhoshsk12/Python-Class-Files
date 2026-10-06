# Variable scope = Scope refers to where a variable is visible and accessible within your program.  
# Scope resolution = (LEGB)  Local -> Enclosed -> Global -> Built-In (**Python looks for in this order only**)

'''
┌───────────────────────────────────────────────┐
│  L  ──►  Local (Inside current function)      │
│  E  ──►  Enclosed (Inside outer function)     │
│  G  ──►  Global (Defined in main script)      │ 
│  B  ──►  Built-in (Built directly into Python)│
└───────────────────────────────────────────────┘
'''
    # Python checks from top to bottom. As soon as it finds a match, it stops looking -> (**Python looks for in this order only**)




    # 1. Local Scope (L)
#          └─ A variable created inside a function belongs to the local scope of that function and can only be used inside it.

def func1():
    a = 1   # Local to func1
    print(a)

def func2():
    b = 2   # Local to func2
    print(b)

func1()     # prints 1
func2()     # prints 2


# What happens if you cross boundaries?

'''def func1():
    a = 1

def func2():
    print(a)''' # 💥 NameError: name 'x' is not defined!

    # --> func2 has no idea that x exists inside func1. Functions cannot see inside each other's local scopes.

print()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    # 2. Enclosed Scope (E)
#          └─ Enclosed scope happens when you have nested functions (a function, defined inside another function).

def func1():
    x = 10      # Enclosed relative to func2

    def func2():
        print(x)    # func2 can see x from its enclosing parent
    func2()

func1() # prints 10



# Visualizing Enclosed scope:
'''
def func1():
   ┌─ x = 10 ─────────────────────────────┐
   │                                      │
   │  def func2():                        │
   │     print(x)  ──► Looks inside func2 │
   │                   (not found)        │
   │                   Looks in parent    │
   │                   (found x = 10)     │
   └──────────────────────────────────────┘
'''

print()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    # 3. Global Scope (G)
#           └─ A variable created outside of all functions is in the global scope. Any function anywhere in that file can read it.


x = 55  # Global variable

def func1():
    print(x)

def func2():
    print(x)

# x = 55  # Global #--> we can declare here also, that is after the both functions (that is also Global)
func1()  # Prints 55
func2()  # Prints 55



    # --- Modifying a Global Variable (global keyword) ---
#           └─ By default, you can read a global variable, but if you try to change it inside a function, Python creates a new local variable instead:

x = 1

def func():
    x = 2   # Creates a LOCAL x, does not change the global x
    print(x)

func()      # prints 2
print(x)    # prints 1 (global x didn't change!)


    # --- To tell Python: "I want to modify the global variable", use the 'global' keyword: ---

# *** Important ***
x = 1

def func():
    global x
    x = 2   # Overwrites the global x!
func()

print(x)    # prints 2
# *** Important ***



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    # 4. Built-in Scope (B)
#           └─ These are names built directly into Python itself (functions and constants like print(), len(), range(), and e from math).

from math import e

# print(e)

def b_func():
    print(e)    # Python finds 'e' in the Built-in scope

b_func()    # Prints 2.718281828459045


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




    # 5: The LEGB Rule in Action (The Priority Test)
#              └─ Watch what happens when we name variables with the same name across different scopes:


from math import e   # built-in (4th)

def b_fun():
    print(e)

e = 500     # Global (3rd)
b_func()
#     -->  # As per the LEGB priority, It takes the Global.




# Another Eg:

x = 3  # Global (3rd)
def func1():
    x = 2  # Enclosed for func2 (2nd)

    def func2():
        x = 1  # Local (1st)
        print(x)

    func2()   # prints 1 (because of Local scope)
func1()



# short visualize:

'''
┌────────────────────────────────────────────────────────┐
│ GLOBAL SCOPE                                           │
│   x = 3                                                │
│                                                        │
│   ┌────────────────────────────────────────────────┐   │
│   │ ENCLOSED SCOPE (Inside func1)                  │   │
│   │   x = 2                                        │   │
│   │                                                │   │
│   │   ┌────────────────────────────────────────┐   │   │
│   │   │ LOCAL SCOPE (Inside func2)             │   │   │
│   │   │   x = 1                                │   │   │
│   │   │                                        │   │   │
│   │   │   print(x) ──┐                         │   │   │
│   │   └──────────────┼─────────────────────────┘   │   │
│   │                  │                             │   │
│   └──────────────────┼─────────────────────────────┘   │
│                      │                                 │
└──────────────────────┼─────────────────────────────────┘
                       ▼

                       
'''

