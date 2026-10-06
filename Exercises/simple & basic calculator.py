# simple and basic calculator.

print("Simple and basic calculator")
print("-------------------------------------")

symbol = input("Enter symbol(+, -, *, /): ")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if symbol == '+':
    print(num1 + num2)
elif symbol == '-':
    print(num1 - num2)
elif symbol == '*':
    print(num1 * num2)
elif symbol == '/':
    print(num1 / num2)
else:
    print("Invalid symbol, enter a valid symbol.")