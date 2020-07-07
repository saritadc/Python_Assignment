# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String: 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result: 'The lyrics is good!'
# 'The lyrics is poor!'


sample = input("Enter string: ")
sample_not = sample.find("not")
sample_poor = sample.find("poor")

if sample_poor > sample_not and sample_not>0 and sample_poor>0:
    sample = sample.replace(sample[sample_not:sample_poor + 4], "good")
    print(sample)
else:
    print(sample)