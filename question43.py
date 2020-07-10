# 43. Write a Python program to remove an item from a tuple

tuple1 = (1,2,2,3,4,5,6)
list1 = list(tuple1)

list1.remove(2)

tuple2 = tuple(list1)
print("Tuple before: ",tuple1)
print("Tuple after: ",tuple2)