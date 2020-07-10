# 34. Write a Python script to merge two Python dictionaries.
dictionary1 = {'a': 100, 'b': 200}
dictionary2 = {'x': 300, 'y': 200}
dictionary3 = dictionary1.copy()
dictionary3.update(dictionary2)
print(dictionary3)

#alt method
dictionary = {}
{dictionary.update(items) for items in (dictionary1, dictionary2)}
print(dictionary)