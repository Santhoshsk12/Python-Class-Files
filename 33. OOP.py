                                    # Creating Class and Object

# object = "Bundle" of related Attributes(variables) and methods(functions)
#           Ex. phone, cup, book
#           need a class to create many objects


# class = (Blueprint) -> used to design the structure and layout of an object




class Car:
    def __init__(self, model, color, year, on_stock):
        self.model = model
        self.year = year
        self.color  = color
        self.on_stock = on_stock


    def drive(self):
        print(f"You can Drive {self.color} {self.model}")

    def stop(self):
        print(f"You can Stop {self.color} {self.model}")


obj = Car("Mustang", "Yellow", 2025, True)    # creating object
obj1 = Car("Nissan", "Blue", 2026, False)    # creating another object

print(obj.model)
print(obj.color)
print(obj.year)
print(obj.on_stock)
print()

print(obj1.model)
print(obj1.color)
print(obj1.year)
print(obj1.on_stock)
print()


obj.drive()
obj.stop()
print()

obj1.drive()
obj1.stop()





# __init__   ---->  runs automatically when Car(...) creates an object. It stores model, year, color and on_stock inside that particular object.

# self   --->  means the current object. For obj.drive(), 'self' refers to 'obj'(self = obj). For obj1.drive(), 'self' refers to 'obj1'(self = obj1).

# ** You only write __init__() when an object needs to store unique data (attributes)—such as a specific model, price, year **

# ** If a class only needs to perform actions (methods) and doesn't store any custom information, __init__() is completely optional **


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# ---- we can create two seperate files (car.py) and (main.py). 
#           we can keep the blueprint(Class) in one file --> car.py
#           and creating object in one file and can access it --> main.py 
#               and then import the file and run.