

import script1

def fav_drink(drink):
    print(f"Favorite drink is {drink}")


def main():
    print("This is script2")

    script1.fav_food("Biriyani")    # important line
    fav_drink("Tea")

    print("Goodbye from script2!")



if __name__ == "__main__":
    main()


    # o/p:  This is script2
    #       Favorite drink is Tea
    #       Favorite food is Biriyani
    #       Goodbye from script2!





# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    # Now, you click RUN on script2.py

# STEP 1: You clicked RUN on script2.py.
#         Python sets script2's secret variable:
#         __name__ = "__main__"

# STEP 2: import script1
#         Python pauses script2 and opens script1.py to read it!






    # What happens inside script1.py right now?

# Because script1 was IMPORTED (not clicked Run directly):
#         Python gives script1: __name__ = "script1"

#         memorizes fav_food
#         memorizes main

#         if __name__ == '__main__':
#                  Python checks: Is "script1" == "__main__"?
#                  Answer: FALSE! ❌

#         Because it is False,
#         It does NOT run script1's main()! It doesn't print pizza!



    # Python returns to script2.py:

# STEP 3: def fav_drink(drink):
#         Python memorizes fav_drink.

# STEP 4: def main():
#         Python memorizes script2's main.

# STEP 5: if __name__ == '__main__':
#         Python checks script2's secret variable:
#         Is "__main__" == "__main__"?
#         Answer: TRUE! ✅

# STEP 6: runs script2's main()!
#         │
#         ├──► prints: "This is script2"
#         │
#         ├──► script1.fav_food("Biriyani")
#         │       Python jumps into script1's recipe and runs it:
#         │       prints: "Favorite food is Biriyani"
#         │
#         ├──► fav_drink("Tea")
#         │       runs the particular line:
#         │       prints: "Favorite drink is Tea"
#         │
#         └──► prints: "Goodbye from script2!"

# PROGRAM FINISHED.
