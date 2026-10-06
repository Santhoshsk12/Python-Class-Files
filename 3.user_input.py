name = input("Enter your Name: ")
age = int(input("Enter your Age: ")) # here, we typecast input string to int

print(f"Your Name is: {name}")
print(f"You are {age + 1} years old") # if we typecast to int, then only we'll able to add 



#Ex: 1 -> Shopping Cart

item = input("Enter your Item: ")
price = float(input("Enter the Price: "))
quantity = float(input("Enter the Quantity: "))

total = quantity * price

print("---------------------------")
print(f"You have bought {quantity} * {item}'s and the price is {price}")
print(f"Total = {total}")