menus = {
    "popcorn": 100.50,
    "chips": 50.00,
    "soda": 40.25,
    "samosa": 20.00,
    "chocolate": 10.00
}

cart = []
total = 0

print("----- MENUS -----")
for key, value in menus.items():
    print(f"{key:12}: Rs.{value:.2f}")
print("---------------")

while True:
    food = input("Enter your food (q to quit): ").lower()
    if food == 'q':
        break
    elif menus.get(food) != None:             # or use -> is not
        # cart += food      # don't do like this
        cart.append(food)
# print(cart)

print()

    # 1. Displaying cart's foods
# print("----- YOUR ORDER -----")
# for food in cart:
#     total = menus.get(food)
#     print(food, end=" ")
# print()
# print("--------------------")


    # 2. Displaying cart's foods and prices -> (side by side)
print("----- YOUR ORDER -----")
for food in cart:
    price = menus.get(food)
    total += price
    print(f"{food:12}: Rs.{price:.2f}")
print()
print("--------------------")
  

print(f"The Total is: Rs.{total:.2f}")