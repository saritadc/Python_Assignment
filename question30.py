# 30. Write a Python script to check whether a given key already exists in a
# dictionary.

dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = int(input("Enter a key: "))

if key in dictionary:
    print("This key already exist in dictionary")
else:
    print("This key doesn't exist")
