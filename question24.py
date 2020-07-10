# 24. Write a Python program to clone or copy a list.

def clone_list(list1):
    cloned_list = list1[:]
    return cloned_list

list1 = list(input("Enter  list items: "))
list2 = clone_list(list1)
print("Original list: ", list1)
print("Cloned list: ", list2)


