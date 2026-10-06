# Typecasting = The process of converting a value / variable from one data type to another
#               str(), int(), float(), bool()
#               Explicit and Implicit


# type() -> for checking data types
name = "Santhosh"
print(type(name))


# -------EXPLICIT CASTING--------
age = 21
gpa = 8.5
is_student = True

# typecasting gpa from float -> int
gpa = int(gpa) 
print(gpa) 

# typecasting age from int -> float
age = float(age)
print(age) # 21.0

# typecasting age from int -> string(str)
age = str(age)
print(age)
print(type(age))

# Typecasting is_student from bool -> str
is_student = str(is_student)
print(is_student)   # True
print(type(is_student))     # <class 'str'>

# typecasting age from int -> bool

    # if age has any value like 21 or -1000000 it returns -> True
    # if age has 0 then it returns -> False
        # True -> 1    False -> 0
age = bool(age)
print(age)      # True
print(type(age))    # <class 'bool'>


# typecasting name from str -> bool

# name = "Santhosh"     # it returns -> True, because it has values -> name = "Santhosh"
name = ""               # it returns -> False, because no values -> name = ""
name = bool(name)
print(name)     # if it has any value it returns -> True 
print(type(name))



# -------IMPLICIT CASTING--------
# Ex: 1
x = 2
x = "Sandy"
        # here, first x = 2 is int,,, then x = "sandy" it becames string

print(x)
print(type(x))


# Ex: 2
x = 2
y = 2.0

x = x/y # here, divides and store the result in x , here now x is changed from int to float
print(x)
print(type(x))
