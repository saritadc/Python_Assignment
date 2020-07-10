# 28. Write a Python script to add a key to a dictionary.
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}

sample = {0:10, 1:20}
new_key = int(input("Enter a new key : "))
new_value = int(input("Enter a new value: "))
print("Before dictionary:", sample)
sample.update({new_key:new_value})
print("After dictionary: ", sample)