# 17. Write a Python program to multiplies all the items in a list.

def multiply_items(lists):
    multiply =  1
    for items in lists:
        multiply *= items

    return print(multiply)

multiply_items([1,3,4])
