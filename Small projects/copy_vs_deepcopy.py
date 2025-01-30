import copy

original_list = [1, 2, [3, 4]]
og2 = original_list
# Shallow copy
shallow_copy = copy.copy(original_list)

# Deep copy
deep_copy = copy.deepcopy(original_list)

# Modify the nested list in the shallow copy
shallow_copy[2][0] = 5
shallow_copy[1] = 3
og2[0] = 0

# Modify the nested list in the deep copy
deep_copy[2][0] = 6

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)
print(og2)