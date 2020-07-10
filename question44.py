# 44. Write a Python program to slice a tuple

sample_tuple = (1,2,3,4,5,6,6,7)
start_index = int(input("Enter start index for slicing: "))
end_index = int(input("Enter end index for slicing: "))


sliced_tuple = sample_tuple[start_index:end_index]
print("Sliced part of tuple: ",sliced_tuple)
print("Tuple after sliced: ",sample_tuple)
