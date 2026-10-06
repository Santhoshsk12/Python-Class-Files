import time  # Importing time module

my_time = int(input("Enter time in seconds: ")) # 5
for i in range(my_time):
    print(i)
    time.sleep(1) # delays 1 second

print("BLAST💥")        # o/p: 0 1 2 3 4 BLAST


# reversed()
my_time = int(input("Enter time in seconds: ")) # 5
for i in reversed(range(my_time)):
    print(i)
    time.sleep(1)  # delays 1 second
print("BLAST💥")           # o/p: 4 3 2 1 0 BLAST



print()


# Eg: (mentioning the ranges)
my_time = int(input("Enter time: "))
for i in reversed(range( 1, my_time + 1 )):  # giving range (1 and input no + 1)
    print(i)
    time.sleep(1)  # delays 1 second
print("BLAST💥")


# final and crt one
# prints without using reversed() keyword
my_time = int(input("Enter time in seconds: "))
for i in range(my_time, 0, -1):   # Count backwards from my_time down to 1
    print(i)
    time.sleep(1) 
print("BLAST💥") 





time.sleep(3) # delays 3 seconds and in 4th second it prints.
print("welcome!")
