# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

def change_string():
    sample = input("Enter a string: ")
    return sample[-1] + sample[1:-1] + sample[0]


print(change_string())
