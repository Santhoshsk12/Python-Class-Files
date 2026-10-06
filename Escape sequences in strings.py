# Escape Sequence in Strings

# \ followed by a character -> is an escape sequence. Let us see the most common escape characters:

# \n: new line
# \t: Tab means(8 spaces)  ---------|
# \\: Back slash                    |
# \': Single quote (')              |
# \": Double quote (")              |
#                                   |
    # 1. Code Indentation (Writing Code)
# \t -> is 4 spaces

    # 2. Literal Tab Characters (\t inside Strings)
# \t -> is 8 spaces



# Eg:
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
# I hope every one is enjoying the Python Challenge.
# Are you ?
# Days  Topics  Exercises
# Day 1	5	    5
# Day 2	6	    20
# Day 3	5	    23
# Day 4	1	    35
# This is a backslash  symbol (\)
# In every programming language it starts with "Hello, World!"