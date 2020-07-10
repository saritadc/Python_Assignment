# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list: [1, 2, 3, 4], string: emp
# Expected output: ['emp1', 'emp2', 'emp3', 'emp4']

def insert_item(list1, string):
    return [string.format(item) for item in list1]

list2 = insert_item([1,2,3,4],"emp{}")
print(list2)