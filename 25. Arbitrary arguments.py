# *args: Allows you to pass multiple non-key (positional) arguments. It packs them into a tuple ().
# **kwargs: Allows you to pass multiple keyword-arguments. It packs them into a dictionary {}.


    # Note on naming: The word 'args' or 'kwargs' is just convention. The real magic is the unpacking operator:
        # Single asterisk (*) = tuple
        # Double asterisk (**) = dictionary



    # Problem:
def add(a, b):
    return a + b

# This works for add(1, 2). But what if you want to add 3 numbers? 4 numbers? 10 numbers? 
# You would get an error because Python only defined 2 parameters.


    # Solution:
        # Place * before the parameter name:  



                            # 1.  *args   --> (Packing Positional Arguments into a Tuple)


def sum(*args):
    print(type(args))  
sum(1, 2, 3)
#               0/p: <class 'tuple'>
#                       => inside the function '*args'  acts/packs as a tuple().


def add(*nums):
    print(type(nums))
    return nums

res = add(1, 2, 3)
print(res)              # o/p: (1, 2, 3)  -> tuple
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    # so we can do iteration:
def sum(*args):
    for arg in args:
        print(arg)

sum(1, 2, 3)
print()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Eg:
def sum(*args):

    total=0
    for arg in args:
        total += arg
    return total

print(sum(1, 2, 3, 4))

# we can use any names for parameters

def sum(*nums):
    total=0
    for num in nums:
        total += num
    return total

print(sum(1, 2, 3))       # 6
print(sum(1, 2, 3, 4, 5)) # 15
print(sum(1))             # 1

print()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Eg: -> String Example: Displaying a Name:

def get_name(*names):
    print(names)        # o/p: ('Hello,', 'Santhosh', 'Kumar')  -> tuple()

    for name in names:
        print(name, end=" ")    # o/p: Hello, Santhosh Kumar

get_name("Hello,", "Santhosh", "Kumar")

                        # -> Whether you pass 2 names or 5 names, *args scoops them all into a tuple and prints them cleanly.

print()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




                        # 2.   **kwargs   --> (Packing Keyword Arguments into a Dictionary)

#      While *args handles 'standalone values', **kwargs handles 'key=value' pairs.



def name(**kwargs):
    print(type(kwargs))   # o/p: <class 'dict'>   --> dictionary

    print(kwargs)       # o/p: {'greet': 'Hello,', 'first': 'Ravi', 'last': 'Varman'}  --> dictionary

name(greet = "Hello,",
     first = "Ravi",
     last = "Varman")



print()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Eg:

def address(**kwargs):
    print(kwargs)         # o/p: {'No': '3', 'Street': 'Main Street', 'city': 'Main City', 'state': 'chennai'}  ---> packed into  ->  Dictionary{}

    for key, value in kwargs.items():       # kwargs.items() -> is important 
        print(f"{key} : {value}")

    # key:value pairs
address(No ="3",     # give number 3 inside doublequotes "", that is crt 
        Street = "Main Street",
        city = "Main City",
        state = "chennai")


# Because kwargs is a dictionary, you can use all standard dictionary methods:

    # 1. kwargs.keys() to see the labels
    # 2. kwargs.values() to see the data
    # 3. kwargs.items() to get key-value pairs
print()
print()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                        # 3. Combining Both *args and **kwargs  --> Tuple + Dictionary
                
    # *** Order Rule: 'Standard parameters'(positional arguments) come first, then '*args', and finally '**kwargs'     ***


# def greetings_and_address(**kwargs, *args):      # It's wrong

def greetings_and_address(*args, **kwargs):        # It's correct
    for arg in args:
        print(arg, end=" ")
    print()

    for value in kwargs.values():
        print(value)

greetings_and_address("Hello,", "Santhosh", "Kumar",
                      no = "3",  
                      street = "Main Street",
                      city = "Main City",
                      state = "chennai")

print()






def greetings_and_address(*args, **kwargs): 
    for arg in args:
        print(arg, end=" ")
    print()



    print(f"{kwargs.get('no')}, {kwargs.get('apt')}")   # is there is no 'apt' key means, python returns -> None
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}")
    print()



# if there is no 'apt' key and getting that means, pythons returns -> None
    # to avoid this, we use if-else

    if "apt" in kwargs:
        print(f"{kwargs.get('no')}, {kwargs.get('apt')}")   # ('No') -> use single quotes for 'No', use single quotes inside f-string's double quotes
    else: 
        print(f"{kwargs.get('no')}")

    print(f"{kwargs.get('street')}, {kwargs.get('city')}, {kwargs.get('state')}")


greetings_and_address("Hello,", "Santhosh", "Kumar",
                      no = "3",  
                    #   apt = "#100",
                      street = "Main Street",
                      city = "Main City",
                      state = "chennai")




 


