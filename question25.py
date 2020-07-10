# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list: [{}, {}, {}]
# Return value: True
# Sample list: [{1, 2}, {}, {}]
# Return value: False

def check_list(list1):

    if all(not d for d in list1):
        print("All dictionaries in a list are empty.")
    else:
        print("All dictionaries  are not empty.")


check_list([{}, {}, {}])
check_list([{1, 2}, {}, {}])
