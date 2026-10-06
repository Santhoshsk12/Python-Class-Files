# collection = single "variable" used to store multiple values
#    set = {} unordered, immutable, No duplicates, but -> Add / Remove Ok.

    # len()
    # in
    # add()
    # remove()
    # pop()
    # clear()

fruits = {"apple", "banana", "mango", "kiwi"}
# fruits = {"apple", "banana", "mango", "kiwi", "mango"} # -> it doesn't allow duplicates. if duplicates, it removes
#                                               o/p : {'mango', 'banana', 'kiwi', 'apple'} -> one "mango"   => unordered


# ***important***
# print(fruits[1]) # we can't use indexing in set, because set is unodered



# print(len(fruits))
# print("kiwi" in fruits)

# fruits.add("grapes") # adds an element
# fruits.remove("grapes") # removes the element

# fruits.pop()
fruits.clear() # ***o/p: set()***





print(fruits)