# format specifiers = {value:flags} format a value based on what flags are inserted

# : .(number)f = round to that many decimal places (fixed point)
# :.1% (Percentage) = Multiplies a number by 100 and adds a % sign.

# :(number) = allocate that many spaces with starting zero pad spaces
# :03 = allocate and zero pad that many spaces(only zero not another symbol)

    # :> (Right align) ---> :>10 =  Pushes text to the right side of a 10-character window.
    # :> (Right align) ---> :#>10 =  Adds (#)symbol before/very first and pushes text to the right side of a 10-character window.

    # :< (Left align) ---> :<10 Pushes text to the left side.
    # :> (Right align) ---> :#<10 = Pushes text to the left side of a 10-character window and Adds (#)symbol after/very end.

    # :^ (center align) ---> :^10 = Centers the text
    # :^ (Right align) ---> :_^10 = Adds (_)symbol at front and last and Centers the text of a 10-character.

# :space --> (: ) = If the number is negative, print the minus sign(-). If the number is positive, leave a blank space instead.
# :+ = use a plus sign to indicate positive value ==> (Pro Tip)

# :, (comma separator) = Adds commans at every three digits.
# :_ (Underscore separator) = Adds underscores every three digits (great for clean data exports).

# := = place sign to leftmost positive


price = 54.1209
price1 = -768.096
price2 = 0.756
amt = 10000090

print(f"the price is: Rs {price:.2f}")  # 54.12
print(f"the price is: Rs {price:.3f}")  # 54.121
print(f"the price is: Rs {price2:.1%} \n")  # Multiplies a number by 100 and adds a % sign.

print(f"This price is: {price:10}")  # by default preceeds with spaces -> totally it allocated 10 space memory -> including the front spaces
print(f"This price is: {price:010} \n")         # Preceeds with 0 -> total 10 memory spaces 

print(f"the price is: Rs {price:*>10}")       # :>10 (Right align): Pushes text to the right side of a 10-character window.
print(f"the price is: Rs {price:*<10}")       # symbol (*) comes in right(backside) -> total 10 spaces
print(f"the price is: Rs {price:_^10} \n")    # symbol (_) comes in middle/center -> total 10 spaces

print(f"the price is: Rs {price:+}")       # if positive no. its starts with (+) symbol
print(f"the price is: Rs {price1:+}")    
print(f"the price is: Rs {price1} \n")     # otherwise starts with (-) symbol .Eg

print(f"the price is: Rs {price: }")       # if positive no. its starts with (space)
print(f"the price is: Rs {price1: } \n")   # otherwise starts with (-) symbol .Eg


print(f"The amt is: {amt:,}\n")     # The amt is: 10,000,090
print(f"The amt is: {amt:_}\n")     # The amt is: 10_000_090






'''Refer format_specifier_Demo.py file -> for examples and easy understanding exercise'''