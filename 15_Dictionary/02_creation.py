d1 = {1: 'ONE', 2: 'TWO', 3: 'THREE'}

list_of_tuple = [(1, 'ONE'), (2, 'TWO'), (3, 'THREE')]
tuple_of_list = ([1, 'ONE'], [2, 'TWO'], [3, 'THREE'])
list_of_list = [[1, 'ONE'], [2, 'TWO'], [3, 'THREE']]
tuple_of_tuple = ((1, 'ONE'), (2, 'TWO'), (3, 'THREE'))

print(dict(list_of_tuple))
print(dict(tuple_of_list))
print(dict(list_of_list))
print(dict(tuple_of_tuple))

print(dict(name='Alice', age=25, city='New York'))


d1 = dict(name='Alice', age=25, city='New York')
d2 = { x: y for x, y in list_of_tuple}
print(d2)