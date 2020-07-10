# 36. Write a Python program to sum all the items in a dictionary.

dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
sum = 0
for key, value in dictionary.items():
    sum += value
print("Sum of values = ",sum)