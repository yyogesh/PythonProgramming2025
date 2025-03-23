s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}

# [] list
# () tuple
# {} set

print(s1)
print(type(s1))

# print(s1[0])  # TypeError: 'set' object is not subscriptable
# print(s1[1:10])  # TypeError: 'set' object is not subscriptable

s2 = set((1, 2, 3, 4, 5, 6, 7, 8, 9))
print(s2)

s3 = set('python') # {'p', 'n', 't', 'y', 'h', 'o'}
print(s3)

s4 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s4)

s5 = {"abc", "def", "ghi", "jkl", "mno", 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(s5)

# mutable
# unordered
# no duplicate elements
# no indexing
# no slicing
# heterogeneous elements
# growable

# s5[0] = 10  # TypeError: 'set' object does not support item assignment
# print(s5)

s5.add(10)
print(s5)
print(len(s5))

s = {10, 20, 30, 40, 50}
print(s) #{50, 20, 40, 10, 30}
s.add(60)
print(s)
s.add(70)
print(s)
s.add(18)
print(s)

# x % 64
print(dir(set))

# s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# a = {1, 2, 3, 5, 7}  A < s


A = {1, 2, 3, 5, 7}
B = {2, 4, 6, 8, 10}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

print(A.intersection_update(B))
print(A.issubset(B))  # True
print(A)


S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {1, 2, 3, 5, 7}
B = {2, 4, 6, 8, 10}

print(A|B)
print(A&B)
print(A-B)
print(A^B)

print(A<S)
print(S<=S)
print(2 in B)

# A = A|B
# print(A)

# A|=B 

# # += 

s1 = {10, 20, 30, 40, 50, 60, 70, 80}
s1.add(90)
print(s1)

s1.add((100, 110))
print(s1)

s2 = s1.copy()
print(s2)

s1.update({120, 130, 140, 150})
print(s1)

s1.update((160, 170, 180, 190))
print(s1)

s1.update('python')
print(s1)

s1.remove(10)
print(s1)

s1.pop()
print(s1)

s1.discard(100)
print(s1)

s1.clear()
print(s1)

print({x for x in range(1, 11)})
print({x**2 for x in range(1, 11)})

s1 = {10, 20, 30, 40, 50, 60, 70, 80}
print({x: x**2 for x in s1})

# [] list
# () tuple
# {} set set()
# {} dict