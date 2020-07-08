# 11. Write a Python program to count the occurrences of each word in a given
# sentence.

def count_words():
    sample = input("Enter a sentence: ")
    words = sample.split()
    counts = dict()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        
    return counts


print(count_words())


