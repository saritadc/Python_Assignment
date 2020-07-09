# 18. Write a Python program to get the largest number from a list. 
def sort_list(lists):
    lists.sort(reverse=True)
    
    return print(lists[0])

sort_list([1,5,6,8,9])