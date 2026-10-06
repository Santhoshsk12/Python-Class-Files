# 1. Arithmetic Operators

a = 10
b = 3

    # a = a + 2 (we can write as -> a += 2)

print(a+b)
print(a-b)
print(a*b)
print(a/b)   # 3.3333333333333335
print(a // b)  # 3 (ans without decimal no) -> floor division
print(a % b)   # 1 (returns Remainder) -> modulus
print(a**b)  # 1000 (Exponential)




# 2. comparison operators
#               Returns True or False

x = 5
y = 10

print(x == y)
print(x != y)
print(x < y)
print(x > y)




# 3. Logical operators
#               and(&), or(|), not

s = True
r = False

print(s & r) # print(s and r)
print(s | r) # print(s or r)
print(not s)



    # Exercise (Example)

age = 51
is_student = "yes"

if age >= 50:
    print("You're too old")
elif age >= 18 and is_student == "yes":     # and (&)
    print("You got a Discount.")
else:
    print("you are not eligible")