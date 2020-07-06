# 5.Write a Python program to add 'ing' at the end of a given string(length should be at
# least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
# Sample String: 'abc'
# Expected Result: 'abcing'
# Sample String: 'string'
# Expected Result: 'stringly'


sample = input("Enter a string: ")
length = len(sample)
last_char = sample[-3:]
if length >= 3 and last_char != "ing":
    print(sample + "ing")
elif length >= 3 and last_char == "ing":
    print(sample + "ly")
elif length < 3:
    print(sample)
