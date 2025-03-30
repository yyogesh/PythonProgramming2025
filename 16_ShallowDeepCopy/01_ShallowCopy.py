# assigning a list to a new variable name doesn't create a copy. Both variables point to the exact same list object in memory. 
# Changes made through one variable are visible through the other.
import copy


original_list = [1, 2, [10, 20]]
assigned_list = original_list

assigned_list[2].append(30)

print("Original List:", original_list)
print("Assigned List:", assigned_list)

assigned_list.append(4)

print("Original List:", original_list)
print("Assigned List:", assigned_list)

print(id(original_list), id(assigned_list), original_list is assigned_list)

print(id(original_list[2]), id(assigned_list[2]), original_list[2] is assigned_list[2])


# Shallow copy
# Create a new list object with the same elements as the original list.
original_list = [1, 2, ['a', 'b']]
shallow_copy1 = original_list.copy()
shallow_copy2 = original_list[:]
shallow_copy3 = copy.copy(original_list)
shallow_copy4 = list(original_list)

shallow_copy1[2].append('c')
shallow_copy2.append(4)
original_list.append(3)

print("Original List:", original_list)
print("Shallow Copy 1:", shallow_copy1)
print("Shallow Copy 2:", shallow_copy2)
print("Shallow Copy 3:", shallow_copy3)
print("Shallow Copy 4:", shallow_copy4)

print("-" * 50)

# Deep copy
original_list = [1, 2, ['a', 'b']]
deep_copy = copy.deepcopy(original_list)

deep_copy[2].append('c')
original_list.append(3)

print("Original List:", original_list)
print("Deep Copy:", deep_copy)

