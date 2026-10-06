# super() function = It is a built-in Python tool, used in a child class to call methods from its parent class (also known as the super-class).

    # super().__init__(...)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Eg: The Problem Without super()
# Imagine you are building a geometric shape program with three shapes:
            # Circle (has a color, filled status, and a radius)
            # Square (has a color, filled status, and a width)
            # Triangle (has a color, filled status, width, and height)
# Notice what they all share: color and filled.


# Look at the messy, copy-pasted code without super():

class Circle:
    def __init__(self, color, filled, radius):
        self.color = color      # Repeated!
        self.filled = filled    # Repeated!
        self.radius = radius

class Square:
    def __init__(self, color, filled, width):
        self.color = color      # Repeated!
        self.filled = filled    # Repeated!
        self.width = width

class Triangle:
    def __init__(self, color, filled, width, height):
        self.color = color      # Repeated!
        self.filled = filled    # Repeated!
        self.width = width
        self.height = height



# The Solution Using super()

    # We create a parent class called 'Shape' to handle color and filled. 
    # Then, every child class uses super().__init__() to hand those two values up to the parent!


# PARENT CLASS
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

# CHILD 1
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)  # Hands color & filled to Shape!
        self.radius = radius             # Keeps radius for itself

# CHILD 2
class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)  # Hands color & filled to Shape!
        self.width = width               # width

# CHILD 3
class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)  # Hands color & filled to Shape!
        self.width = width               # width
        self.height = height             # height


# circle = Circle("red", True, 5)

circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=False, width=6)
triangle = Triangle(color="yellow", filled=True, width=7, height=8)

# From parent Shape:
print(circle.color)     # red
print(square.filled)    # False

# From child unique attributes:
print(circle.radius)    # 5
print(square.width)     # 6
print(triangle.width)   # 7
print(triangle.height)  # 8


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Using super() with Regular Methods (Not Just __init__)
    # super() isn't only for __init__. You can also use it to call regular parent methods and extend them!

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def des(self):
        # 1. Call the parent's describe method first!
        super().describe()
        # 2. Add extra circle-specific information!
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius:.2f}cm^2")

circle = Circle("red", True, 5)
circle.des()



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
* super()	                           References the parent / super-class.
* super().__init__(...)              Delegates common attribute initialization to the parent class constructor.
* super().method()	               Runs the parent's version of a method before or after child logic.

    Notice syntax:  	You do not pass self into super().__init__() --Python passes self automatically!
'''