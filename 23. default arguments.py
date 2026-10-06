# Default arguments = A default argument is a backup value.
#                       If you forget to provide a value when calling a function, 
#                           Python won't throw an error—it will simply use the --default backup value-- you set ahead of time.



import time
def counter(end, start=0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("END!")

counter(5, 2)   # giving both arguments ->  end=5 and start=2
                        # start becomes 2, end is 5
counter(5)      # giving end=5 only, start=0 by 'default'
                        # start is automatically 0, end is 5.



# **The Golden Rule (Don't Break This!)**

    # Rule: 'Non-default arguments' must come first. 'Default arguments' must come at the very end.




# ❌ ILLEGAL - SyntaxError!
def count(start=0, end):
    pass

# ✅ LEGAL
def count(end, start=0):
    pass

# Why? If Python allowed count(start=0, end) and you ran count(10), 
#   Python wouldn't know if 10 was meant for start or end. Putting required items first keeps the ordering unambiguous.



