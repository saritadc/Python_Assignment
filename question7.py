# 7.Write a Python function that takes a list of words and returns the length of the
# longest one.

def find_longest_word(words_list):
    words_len = []
    for item in words_list:
        words_len.append((len(item), item))
    words_len.sort(reverse=True)
    return words_len[0][0]

print(find_longest_word(["abc", "sbchs", "abcdefgh"]))
