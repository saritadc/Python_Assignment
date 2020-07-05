# 1. Write a Python program to char_frequency the number of characters (character
# frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

sample = input("Enter sample string: ")
char_frequency = {}
for char in sample:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
char_sorted = sorted(char_frequency.items(),
                     key=lambda keyvalue: keyvalue[1], 
                     reverse=True)
print(dict(char_sorted))




