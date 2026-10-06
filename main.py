from car import Car     # Importing line is very very important here


car1 = Car("BMW", "Black",  2026)
car2 = Car("Mustang", "Red",  2024)

print(car1.model)
print(car1.color)
print(car1.year)

car1.drive()
car1.stop()
print()


print(car2.model)
print(car2.color)
print(car2.year)

car2.drive()
car2.stop()