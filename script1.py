


def fav_food(food):
    print(f"Favorite food is {food}")


def main():
    print("This is script1 file.")
    fav_food("pizza")
    print("Goodbye from script1!")


if __name__ == "__main__":
    main()



    # o/p:    This is script1 file.
    #         Favourite food is pizza
    #         Goodbye from script1!




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    # You open script1.py in your editor and click RUN.


# STEP 1: You clicked RUN on script1.py.
#         Python sets script1's secret variable:
#         __name__ = "__main__"

# STEP 2: def fav_food(food):
#         Python memorizes the recipe for fav_food. Does not run it yet.

# STEP 3: def main():
#         Python memorizes the recipe for main. Does not run it yet.

# STEP 4: if __name__ == '__main__':
#         Python evaluates: Is "__main__" == "__main__"?
#         Answer: TRUE! ✅

# STEP 5: main() is called!
#         │
#         ├──► prints: "This is script1"
#         ├──► calls fav_food("pizza")
#         │       └──► prints: "Favorite food is pizza"
#         └──► prints: "Goodbye from script1!"

# PROGRAM FINISHED.




