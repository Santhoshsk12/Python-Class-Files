# keyword arguments = explicitly label each value using its parameter name (name=value).
#                        When you use keyword arguments, the order no longer matters at all.


    # Until now, we have used 'positional arguments'. That means Python figures out which variable gets which value based on the order you type them in:


# E.g: 
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# Positional arguments:
hello("Hello", "Mr.", "Santhosh", "Kumar")

hello("Kumar", "Hello", "Mr.", "Santhosh")
# Prints: "Kumar Hello Mr. Santhosh"   ->  (Nonsense!)





#  using pure keyword arguments:
def msg(greet, first, last):
    print(f"{greet}, {first} {last}")

msg(last="Kumar", greet="Hello", first="Santhosh")
#               o/p: Hello, Santhosh Kumar




# Mixing Positional and Keyword Arguments:
    # **The Golden Rule: 'Positional arguments' must come first. 'Keyword arguments' must follow after.**

# ✅ Legal: "Hello" is positional (first slot), the rest are labeled keywords
msg("Hello", title="Mr.", last="Kumar", first="Santhosh")

# ❌ ILLEGAL - SyntaxError: positional argument follows keyword argument
msg(title="Mr.", "Hello", last="Kumar", first="Santhosh")




# The sep (Separator) Keyword:
    # By default, when you print multiple items separated by commas, Python puts a space between them. You can change that delimiter using sep:

print("1", "2", "3", "4", "5", "6", sep="-")
#                                  o/P: 1-2-3-4-5









# Real Exercise — Generating a Phone Number
    # --(mixed arguments -> positional and keyword arguments) / and 'sep' (separator) keyword--

def phone_no(country, area, first, last):
    return(f"{country}-{area}-{first}-{last}")

# res = phone_no(country=1, area=123, first=456, last=789) or 
res = phone_no(1, area=123, first=456, last=789)
print(res)
