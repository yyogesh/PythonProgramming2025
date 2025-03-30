d1 = {1: 'ONE', 2: 'TWO', 3: 'THREE'}

print(d1)

print(d1[1])

d1[4] = 'FOUR'

print(d1)

for key in d1:
    print(key)

for key in d1:
    print(key, d1[key])


empty_dict = {}
print(empty_dict)

empty_dict = dict()
print(empty_dict)

d2 = {1: 2, 2.5: True, 'a': [1, 2, 3], (1, 2): 'tuple', 5+6j: 'complex'}
print(d2)

print(d2[1])
print(d2[2.5])
print(d2['a'])
print(d2[(1, 2)])
print(d2[5+6j])

d3 = { 1: [10, 11], 2: (4,5), 3: {8, 9}, 4: {1: 2, 3: 4}}
print(d3)

d4 = {(1, 2): 'tuple'} # immutable
print(d4)

d5 = {[1, 2]: 'list'} # mutable 
print(d5)

# dictionary with list as key
# d6 = {[1, 2]: 'list'} # TypeError: unhashable type: 'list'

# list, set, dict are mutable and unhashable
# tuple, str, int, float are immutable and hashable