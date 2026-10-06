x = 3.14
y = -4
z = 5

print(round(x))
print(abs(y))   # absolute -> turns the -ve into +ve
print(pow(4, 3))    # power -> 4 is base, and 3 is exponential ==> 4 power 3. i.e: (4**3)
print(max(x, y, z)) # 5
print(min(x, y, z)) # -4




    # math module
import math

a = 9
b = 9.1
c = 9.9

print(math.pi)
print(math.e)
print(math.sqrt(a))     # 3.0

print(math.ceil(b))     # always rounds up -> 10
print(math.floor(c))    # always round down -> 9





    # Exercise

"""1.circumference of a circle"""

import math

radius = float(input("Enter radius: "))
circumference = 2 * math.pi * radius

print(f"Circumference is: {round(circumference, 2)}cm")




"""2.Area of a circle"""

import math

radius = float(input("Enter radius: "))
area = math.pi * pow(radius, 2)

print(f"Area is: {round(area, 2)}cm^2")
