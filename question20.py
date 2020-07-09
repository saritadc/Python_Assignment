# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List: ['abc', 'xyz', 'aba', '1221']
# Expected Result: 2
def count_item(lists):
    count = 0

    for items in lists:
        if items[0] == items[-1]:
            count += 1

    return print(count)


count_item(['abc', 'xyz', 'aba','1221', 'abva'])
