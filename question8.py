# 8. Write a Python program to remove the nth index character from a nonempty
# string.

def remove_char(sample, nth_index):
    first_part = sample[:nth_index]
    last_part = sample[nth_index + 1:]
    return (first_part + last_part)

print(remove_char("string", 0))
print(remove_char("character", 3))


