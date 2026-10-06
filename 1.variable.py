# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
first_name = "Raj"
food = "Idle"
email = "Raj123@fake.com"

print(f"Name is {first_name}")
print(f"you food is: {food}")
print(f"Email is: {email}")

# Integers
age = 21
quantity = 3
no_of_students = 10

print(f"your are {age} years old")
print(f"The Quantity of Apples: {quantity}")
print(f"Your class has {no_of_students} students")

# Float
price = 999.99
distance = 4.5
gpa = 8.5

print(f"You travelled {distance}km")
print(f"The price is Rs.{price}")
print(f"Your gpa is: {gpa}")

# Boolean  ->  True / False
is_online = True
is_online = False
print(f"Are you Online?: {is_online}")

# ---------------------------------------
is_student = True

if is_student:
    print("You are a Student.")
else:
    print("You are NOT a Student.")