# Membership Operators = Membership operators are used to test whether a value or variable is found inside a sequence or collection 
#                           (such as strings, lists, tuples, sets, or dictionaries).

# They return a boolean value: either True or False.
    # 1. in:        Returns True if the item is present inside the collection.
    # 2. not in:    Returns True if the item is not present inside the collection.



    # 1. Membership Operators with Strings
# Eg: -> in

word = "APPLE"    # --> string
letter = input("Enter a letter: ")

if letter in word:
    print(f"There is a '{letter}'")
else:
    print(f"{letter} was not found.")



print()

# Eg: -> not in
email = "hello@gmail.com"       # --> string

if '@' not in email and '.' not in email:
    print(f"{email} is not valid")
else:
    print(f"It is a valid email -> {email}")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    # 2. Membership Operators with Sets, Lists, and Tuples
# We can check whether a specific element belongs to a collection of items.


# Eg: -> in
students = {"Ravi", "Ram", "Deepak", "Raghul"}   # --> set{}

student = input("Enter Student name: ")

if student in students:
    print(f"{student} was found.")
else:
    print(f"{student} was not found.")


# Eg:  -> not in

students = {"Ravi", "Ram", "Deepak", "Raghul"}   # --> set{}
student = input("Enter Student name: ")

if student not in students:
    print(f"{student} was not found.")
else:
    print(f"{student} was found.")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    # 3. Membership Operators with Dictionaries
# Dictionaries are special because they contain both 'keys' and 'values'. By default, in checks the 'keys'.


grades = {"Ravi" : "A",
          "Raj" : "B",
          "Ram" : "C",
          "Doom" : "A"}

stu = input("Enter Student name: ")

if stu in grades:
    print(f"{stu}'s grade is {grades[stu]}")     # indexing -> (variable) -> grades[stu] 
#                                                   grades[stu] uses the variable -> stu.
#                                  (or) 
    print(f"{stu}'s grade is {grades.get(stu)}")     # using get() method of dictionary
#                                  (❌ don't use this)
    print(f"{stu}'s grade is {grades.get('stu')}")   # ❌ don't use/write like this -> ('stu') -> using single quotes, inside () -> for stu
#                                                           --> grades.get('stu') with quotes looks for the literal word "stu" as a key!
#                                                              Because there is no key named "stu" inside the dictionary, grades.get('stu') returns --> None.
else:
    print(f"{stu} is not found.")



# ❌ INCORRECT (Looks for the literal word "stud"):
grades.get('stu')   # Returns None!

# ✅ CORRECT (Uses the variable without quotes):
grades.get(stu)     # Returns "A" (if stu = "Ravi")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. grades[student] (Square Brackets)   ----->    ** If key is NOT found  ==> Crashes the program with a 'KeyError' **  ----->   ** Cannot set a fallback **
# 2. grades.get(student) (get method)    ----->    ** Returns 'None'       ==> (no crash) **                              ----->   ** Can set a fallback: grades.get(student, "Not Found") **

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    # Another Eg:

registered_usernames = ["name123", "123name", "name@123"]   #  --> list[]
username = input("Enter username: ")

if username in registered_usernames:
    print(f"Sorry, '{username}' is already taken. Please pick another.")
else:
    print(f"Welcome, '{username}'! Your account has been created.")



