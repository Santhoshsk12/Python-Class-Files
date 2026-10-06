    # 3. Displaying cart's foods and prices -> (down) below the cart's foods


menus = {
    "popcorn": 100.50,
    "chips": 50.00,
    "soda": 40.25,
    "samosa": 20.00,
    "chocolate": 10.00
}

cart = []
prices = []
total = 0

print("----- MENUS -----")
for key, value in menus.items():
    print(f"{key:10}: Rs.{value:.2f}")
print("---------------")


while True:
    food = input("Enter your food(q to quit): ").lower()
    if food == 'q':
        break
    elif menus.get(food) is not None:
        cart.append(food)

        prices.append(menus.get(food)) # **important**



print("----- YOUR ORDERS -----")

# Display cart's foods
print("Items : ", end=" ")
for food in cart:
    print(food, end=" ")
print()


# Display cart's food prices
print("Prices: ", end=" ")
for price in prices:
    print(f"Rs.{price:.2f}", end=" ")
    total += price
print()


print("---------------")
print(f"The Total is: Rs.{total}")




# o/p:
'''
----- MENUS -----
popcorn   : Rs.100.50
chips     : Rs.50.00
soda      : Rs.40.25
samosa    : Rs.20.00
chocolate : Rs.10.00
---------------
Enter your food(q to quit): chips
Enter your food(q to quit): soda
Enter your food(q to quit): apple
Enter your food(q to quit): samosa
Enter your food(q to quit): chocolate
Enter your food(q to quit): q
----- YOUR ORDERS -----
Items :  chips soda samosa chocolate 
Prices:  Rs.50.00 Rs.40.25 Rs.20.00 Rs.10.00 
---------------
The Total is: Rs.120.25
'''