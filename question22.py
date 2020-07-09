# 22. Write a Python program to remove duplicates from a list.

def remove_duplicate(lists):
    for item in lists:
        if lists.count(item) >=2:
            lists.remove(item)
        
    print(lists)

remove_duplicate([1,1,3,4,5,3,4])