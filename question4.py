# 4.Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
# Sample String: 'abc', 'xyz'
# Expected Result: 'xyc abz'

string_one = input("Enter first string: ")
string_two = input("Enter second string: ")

string_swap1 = string_one.replace(string_one[0:2], string_two[0:2])
string_swap2 = string_two.replace(string_two[0:2], string_one[0:2])

print(string_swap1+ " " + string_swap2)
