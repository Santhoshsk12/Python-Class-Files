# Instance Variable = A variable defined inside the constructor (__init__) using self.. 
#                       It belongs to only that one specific object. (Eg: Each car has its own unique 'color' or 'model').
#                       Access -->  object.variable (e.g., car1.model)


# Class Variable = A variable defined outside the constructor, directly inside the class body. 
#                   It is shared equally by all objects created from that class. (Eg: All cars have 4 wheels).
#                      Access --> class.variable (e.g., Car.wheels)




class Car:

    # CLASS VARIABLE (shared by every car made)
    wheels = 4

    def __init__(self, model, year, color, for_sale):
        # INSTANCE VARIABLES (unique to each car)
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Nissan", 2025, "blue", True)

# Accessing instance variables:
print(car1.model)  # Mustang
print(car2.model)  # Nissan

# Accessing the class variable through the objects:
print(car1.wheels)  # 4
print(car2.wheels)  # 4

# ** the industry standard and best practice is to access class variables through the Class name itself: **
print(Car.wheels)   # 4
#          --- Writing like this tells, 'wheels' belongs to the entire class, not just to car1 or car2
print()




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



class Student:

    # CLASS VARIABLES (Shared school-wide)
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        # INSTANCE VARIABLES (Unique to each student)
        self.name = name
        self.age = age

        # Every time a new student(i.e: object) is created, increment the shared counter!
        Student.num_students += 1    #  **----Important----**

student1 = Student("Santhosh", 20)
student2 = Student("Deepak", 23)

print(f"Number of students are: {Student.num_students}")    # 2
print(f"{Student.class_year} graduated class has {Student.num_students} students.")
print("-----------")
print(student1.name)
print(student2.name)




# 1. Student.num_students = 0

# 2. student1 = Student("Santhosh", 20)
#    ├── __init__ runs
#    └── Student.num_students += 1  ──► Counter is now 1

# 3. student2 = Student("Deepak", 23)
#    ├── __init__ runs
#    └── Student.num_students += 1  ──► Counter is now 2

# 4. student3 = Student("Sandy", 27)
#    ├── __init__ runs
#    └── Student.num_students += 1  ──► Counter is now 3