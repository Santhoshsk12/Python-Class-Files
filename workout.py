
# Finding the Largest Number

# 1. using built-in function/method
numbers = [1,7,5,3,9,0]

largest = max(numbers)
print(f"Largest no is: {largest}")



# 2. without using buit-in function/method
numbers = [4,9,2,7,5]
largest = numbers[0] # this is 4 right now

for i in numbers:
    if i > largest:
        largest = i # Update with the bigger number

print(f"The Largest no is: {largest}")





                        # Palindrome

# 1. with using buit-in function/method
word = "mom"
reversed = word[::-1]

if word == reversed:
    print(f"Yes, '{word}' is a Palindrome!")
else:
    print(f"NO, '{word}' is NOT a Palindrome.")



# 2. without using buit-in function/method
word = "123"
check = ""

for i in word:
    check = i + check

if word == check:
    print(f"Yes, '{word}' is a Palindrome!")
else:
    print(f"NO, '{word}' is NOT a Palindrome.")
