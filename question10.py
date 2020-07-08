# 10. Write a Python program to remove the characters which have odd index
# values of a given string.

def remove_odd_index():
    sample = input("Enter a string: ")
    new_sample = "".join([sample[i] for i in range(len(sample)) if i % 2 == 0])
    return new_sample


print(remove_odd_index())