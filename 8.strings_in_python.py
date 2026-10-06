# String - sequence of characters

    # name = 'Santhosh'

# 1
sname = "Ravi varman"

print(sname.upper())
print(sname.lower())
print(sname.capitalize())


# 2. indexing/Slicing
num = "9999999990"

sliced_num1 = num[:2]    # 0 and 1 index ---> 99
sliced_num2 = num[-2:]   # last is -1 and then -2 ---> 90
print(sliced_num1)
print(sliced_num2)

masked_num = num[:2] +"******" +num[-2:]
print(masked_num)



# 3. title() --> makes all starting letter capital and remaining lower case 
song = "shape OF you"
artist = "SANDY sk"

print(f"{song.title()} - {artist.title()}") # Shape Of You - Sandy Sk



# 4. replace()
location = "chennai"
updated_location = location.replace("chennai" , "Pondy")
#                                   old_name    new_name
print(updated_location)



# 5. split() and strip()

'''split() -> it split the string using delimiter(comma, space, dot, or any other characters also)
    and returns output as like the list -> if list means it has index positions'''

msg = "To begin, begin."
# print(msg.split(","))   #['To begin', ' begin.'] -> spliting using comma(,)
#            index   ----->     0           1

    # Getting the value at index position 1, we can write like this....
print(msg.split(",")[1])    # begin.  -> 1st position's index value
 


                # for removing space in front of ' begin.'  --> Method 1 (using split())
print(msg.split(",")[1].split(" ")) #['', 'begin.'] -> Spliting using space(" ")
#                index      --->       0     1

print(msg.split(",")[1].split(" ")[1]) #begin. -> getting the 1st index value

                # for removing space in front of ' begin.'  --> Method 2 (using strip())
'''strip() -> It removes very beginning and very end characters.
    by default, it removes all white space characters like spaces, tab(\t) and newlines(\n)
'''

print(msg.split(",")[1].strip()) #begin. -> without space 


 # split()

quote_msg = "Do what you can, with what you have, where you are."

# print(quote_msg.split(""))  # ValueError: empty separator
print(quote_msg.split())        # ['Do', 'what', 'you', 'can,', 'with', 'what', 'you', 'have,', 'where', 'you', 'are.']
print(quote_msg.split(" "))     # ['Do', 'what', 'you', 'can,', 'with', 'what', 'you', 'have,', 'where', 'you', 'are.']
#                                                           Both are same


# strip()

demo = "    Hello World!     "
crt_demo = demo.strip()
print(crt_demo)     #Hello World!

demo = " \t  Hello World!     \n"
crt_demo = demo.strip()
print(crt_demo)     #Hello World! -> removes spaces and \t and \n


# 6. in

quote = "Do what you can, with what you have, where you are."

if "have" in quote:
    print("Yes it is.")


# 7. find() 
'''find the value or something entered and returns its index no.
    If the value is not found, It returns    -1 '''
print(quote.find("what"))   # 3
print(quote.find("hello"))   # -1

print(quote.find("w"))   # 3 -> finds the first occurance 'w' and returns its index no.
print(quote.rfind("w"))   # 37 -> finds the last occurance 'w' and returns its index no. --> it counts(index no.) from the beginning 

print(quote.find(" "))      # finds the spaces -> 2


# 8.index()
'''find the value or something entered and returns its index no.
    If the value is not found, it throws/shows ERROR  i.e: ValueError'''
    
print(quote.index("what"))  # 3
# print(quote.index("hello"))  # ValueError: substring not found


# 9. len() -> Total length ==> It counts each characters 
print(len(quote))   # 51 -> counts each characters 
print(len(quote.split())) # 11 -> it splits and then counts and gives the length


# 10. isdigit() -> returns True or False
#                      if the string only\fully contains digits(numbers), then returns -> True, otherwise -> False
#                       if it fully contains digits, but has space means -> False 

# digit_check = "hello coder"
# digit_check = "hello123"
# digit_check = "hel lo"
digit_check = "1234"      # True
# digit_check = " 1234"
# digit_check = "1234  "
print(digit_check.isdigit())



# 11. isalpha() -> Returns True or False
#                       if the string only\fully contains alphabets, then -> True, otherwise -> False
#                         if it fully contains Alphabets, but has space means -> False

# alpha_check = "abc123"
# alpha_check = "123"
alpha_check = "sandy"       # True
# alpha_check = "  space"
# alpha_check = "space "
print(alpha_check.isalpha())




# 12. count() -> It counts/tracks how many times a specific element appears within it
#                               It needs the character, symbols or any other to enter 

txt = "Do what you can, with what you have, where you are."
txt1 = "believe-in-yourself-first"

print(txt.count(" "))       # 10  -> 10 spaces
print(txt.count("you"))       # 3 -> 3 "you"

print(txt1.count("-"))         # 3




        # diff btw len() and count()

# Eg-1
quote = "Do what"

print(len(quote)) # 7
print(quote.count(" ")) # 1 -> 1 space


# Eg-2
my_list = ["apple", "banana", "apple", "cherry"]

# len() gives the total count of elements
print(len(my_list))   
# Output: 4

# count() searches for and tallies a specific item
print(my_list.count("apple"))  
# Output: 2









# using this we can able to know all available string methods -> it will comes in Terminal
print(help(str))