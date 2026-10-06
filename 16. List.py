# collection = single "variable" used to store multiple values
#    list = [] ordered, mutable, allows duplicates

    # index[] -> returns the element/value

    # len()
    # in
    # [0] = "element"
    # insert()
    # append()
    # remove()
    # pop()
    # clear()

    # index()
    # count()

fruits = ["apple", "banana", "mango", "papaya"]
# fruits = ["apple", "banana", "mango", "papaya", "mango"] # -> It allows duplicates
#                                       o/p:  ["apple", "banana", "mango", "papaya", "mango"] -> two "mango" => ordered



print(fruits[1]) # we can use indexing in list. o/p: banana

# print(len(fruits))
# print("mango" in fruits)

# fruits[0] = "watermelon" #['watermelon', 'banana', 'mango', 'papaya'] -> it remove the value at index [0] and place/insert a new value (replace)
# fruits.insert(2, "kiwi") # it places/adds the new value at index[2] and moves the already existed value at that index[2] to (side) next index's position.
#                             -> we can able to insert the value at specific index

# fruits.append("pineapple") # adds value at the very end 
# fruits.remove("mango") # removes the particular value 

# fruits.pop() # removes the very-end element/value
# fruits.clear() # it clears/removes everything in the list -> only the empty list exists. ->  o/p: []

# print(fruits.index("mango")) # returns the index number of an element
# print(fruits.count("apple")) # counts the particular element, how many times it is there in list

print(fruits)




# for fruit in fruits:
#     print(fruit)