# 23. Write a Python program to check a list is empty or not.


lists = list(input("Enter a list: "))
if lists:
    print(bool(lists))
    print("List is not empty")
else:
    print(bool(lists))
    print("List is  empty")