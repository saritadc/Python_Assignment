# 38. Write a Python program to remove a key from a dictionary.

dictionary = {'a':1, 'b':4, 'c':6, 'd': 7}
print(dictionary)
key = input("Enter a key to remove from above dictionary: ")
if key in dictionary:
    dictionary.pop(key)
    print(dictionary)
else:
    print("Key is not found")

