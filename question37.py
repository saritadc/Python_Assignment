# 37. Write a Python program to multiply all the items in a dictionary.

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
multiple = 1
for key, value in dictionary.items():
    multiple *= value
print("Multiple of values = ", multiple)
