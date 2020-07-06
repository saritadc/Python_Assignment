# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String: 'restart'
# Expected Result: 'resta$t'

#To change first characcter which has more than one occurances
sample = input("Enter a string: ")
char = sample[0]
sample = sample.replace(char, "$")
sample = char + sample[1:]
print(sample)


# To change every charecter which has more than one occurances 
sample_list = []
sample = input("Enter String: ")
for char in sample:
    if char in sample_list:
        sample_list.append('$')
    else:
        sample_list.append(char)
print(''.join(str(i) for i in sample_list))
                                                                                
