                    # if __name__ == "__main__" 


# What is if __name__ == '__main__':?
# In Python, every file (.py) can be used in two different ways:
    # 1. Run directly as a standalone program (e.g., clicking the "Run" button in PyCharm, or typing python script.py in your terminal).
    # 2. Imported as a 'module' into another file (e.g., import script).



# if __name__ == '__main__':   -->  is a security gate. It tells Python:
    # | "Only run the code inside this block if this file is run directly. 
    # |  If someone imports this file, do not run this code automatically."


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    # The Magic Behind '__name__':
# Python automatically assigns a hidden, built-in string variable named   __name__ (with two underscores on each side, 
#                                                                                    often called "dunder name") to every Python file.


# What value gets stored inside __name__?
'''
               How the script is executed                        What Python stores in __name__
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1.             Run directly by you                                        "__main__"
# 2.             Imported by another script	                 The actual name of the file (e.g., "script1")
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Python has a secret hidden label attached to every .py file called __name__.

# Whenever Python touches a file, it asks one question:
        # "Did the user press RUN on this specific file right now?"


'''
If the answer is YES (you pressed the green run button on this file):
Python gives it the honorary title:
'''

__name__ = "__main__"


'''
If the answer is NO (this file was only pulled in via import by another file):
Python gives it its real file name:
'''

__name__ = "script1"



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# We will create two files: script1.py and script2.py

    # look into the two files -> for codes.





    # ======= look into 'Python's - script execution vs. module imports.txt' file ============ for further explanation and understanding.

