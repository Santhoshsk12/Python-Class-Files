# indexing = accessing elements of a sequence using [] (indexing operator)
#               [start : end : step]

msg = "Good Morning to everyone."
number ="1234567890"

print(msg[5:])  # starting from 5 and goes upto the very end
print(msg[5:12])  # starts from index 5 to 11 --> end means it is excluded 12 -> (12-1 = 11)
print(msg[::-1])    # Reverse the string
print(msg[-9:-1])    # from last

print(number[::2])  # step : 2 -> o/p: 13579