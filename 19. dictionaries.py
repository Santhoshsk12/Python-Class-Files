# Dictionary = {} A collection of {key: value} pairs, separated by a colon (:) --> You can also use the dict() constructor.
#               ordered, immutable, NO duplicates.

    # "Keys" must be immutable types (like strings, numbers, or tuples) and must be unique.
    # "Values" can be of any data type (including lists, tuples, or other dictionaries) and can repeat.


        # get()
        # update()
        # pop()
        # popitem()
        # .keys()
        # .values()
        # .items() -> both keys and values
        # clear()


# Creating a dictionary using literals
user_profile = {
    "username": "coder123",
    "age": 25,
    "skills": ["Python", "SQL"] # here values are lists
}

# Creating an empty dictionary
empty_dict = {}
# or
empty_dict_alt = dict()




meats = {"chicken": "chicken", 
        "mutton": "goat",
        "beef": "cow"}


print(meats.get("mutton"))    # => get(key), returns the key's value.
# print(meats.get("quail"))     # if there is no key that matches, **it returns -> o/p: None**

    # ----Loop through keys (default behavior)----
# for meat in meats:   
#     print(meat)




# meats.update({"pork": "pig"})             # -> we can add new {key: value} pair at end
# meats.update({"chicken": "Chicken"})      # -> we can able to change/replace the value also with the key 

# meats.pop("beef")         # pop(key) -> we can remove specific element by giving 'key' name
# meats.popitem()           # popitem() -> it will remove the very-end element {key: value}




    # ----Getting all keys(like default one)----
# keys = meats.keys()
# print(keys)             # 0/p: dict_keys(['chicken', 'mutton', 'beef'])

# for keys in meats.keys():  # -> iterating each keys one by one
    # print(keys)




    # ----Gettings all values----
    # **Loop through values using .values()**
# values = meats.values()
# print(values)              # o/p: dict_values(['chicken', 'goat', 'cow'])

# for values in meats.values():  # iterating each values one by one
#     print(values)




    # ----Getting both keys and values----
    # **Loop through both using .items()**
# items = meats.items()
# print(items)            # o/p: dict_items([('chicken', 'chicken'), ('mutton', 'goat'), ('beef', 'cow')])

# for items in meats.items(): 
#     print(items)            # o/p: ('chicken', 'chicken')
#                             #      ('mutton', 'goat')
#                             #      ('beef', 'cow')

for key, value in meats.items():
    print(f"{key}: {value}")    # o/p:  chicken: chicken
                                #       mutton: goat
                                #       beef: cow


# meats.clear()  # .clear() - empties the entire dictionary
                # o/p: {}

print(meats)