# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form(alphanumerically).
# Sample Words: red, white, black, red, green, black
# Expected Result: black, green, red, white, red

sample_words = input("Input comma separated sequence of words: ")
words_list = [word for word in sample_words.split(",")]

print(",".join(sorted(list(set(words_list)))))
