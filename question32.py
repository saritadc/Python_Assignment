# 32. Write a Python script to generate and print a dictionary that contains a
# number(between 1 and n) in the form(x, x*x).
# Sample Dictionary(n=5):
# Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

nth_number = int(input("Enter a number between 1 to n as n = "))
dictionary = dict()

for x in range(1, nth_number+1):
    dictionary[x] = x*x

print(dictionary)


