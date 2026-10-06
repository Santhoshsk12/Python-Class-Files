# for loop = executes a block of code for a fixed number of times.
#               we can iterate over a range, string, sequence, etc.



for i in range(1, 6):
    print(i)
print("HAPPY NEW YEAR!")

# reserved()
for i in reversed(range(1, 6)):
    print(i)
print("HAPPY NEW YEAR!")


# start, end, step 
for i in range(1, 11, 2):  # step -> 3
    print(i)


word = "hello all"
for i in word:
    print(i)


        # ***for-else***
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)


print()


    # 1. break and continue  -> continue is different in for-loop, unlike in while-loop.

for i in range(1, 11):
    if i == 5:
        # break          # -> stops and leave everything
        continue      # -> skips that part and continue
    print(i)

    # or using -> else

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(i)



# 2. Pass = In python when statement is required (after semicolon), but we don't like to execute any code there, 
#           we can write the word 'pass' to avoid errors. Also we can use it as a placeholder, for future statements.

for number in range(6):
    pass


print()

# Example:

my_num = int(input("Enter time: "))

# for i in time:    -> don't type like this, it's wrong 
for i in range(my_num):    # time is no.(int) so use range function
    print(i)