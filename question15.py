# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result:
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_string_middle(string1, string2):
    middle_index= int((len(string1))/2)

    return  print(string1[:middle_index] + string2 + string1[middle_index: ])


insert_string_middle('{{}}', 'PHP')
insert_string_middle('[[]]<<>>', 'Python')
