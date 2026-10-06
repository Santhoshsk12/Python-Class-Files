# Inheritance = Inheritance allows a class(called a Child class or Subclass) to inherit attributes and methods from another class(called a Parent class or Superclass).
#               Helps with code reusability and extensibility
#                               -----**  syntax: --> class Child(Parent)  **-----
#               Parent --> has attributes and methods
#               Child -->  automatically inherits all parent class's attributes and methods, and also can have unique methods

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):      # child automatically inherits parent's attributes and methods, and also can have unique methods(speak).
    def speak(self):
        print("BARKS!")

class Cat(Animal):       # child automatically inherits parent's attributes and methods, and also can have unique methods(speak).
    def speak(self):
        print("MEOWS!")




dog = Dog("Scooby")
cat = Cat("Tom")

print(dog.name)
print(dog.is_alive)

dog.eat()
dog.sleep()
dog.speak()
print()

print(cat.name)
print(cat.is_alive)

cat.eat()
cat.sleep()
cat.speak()
print()


