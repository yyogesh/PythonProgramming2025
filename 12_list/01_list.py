list2 = ['a', 'b', 'c', 'd', 'e']
#  List<int> a = new List<int>();
print(type(list2))
print(list2[2])
print(list2[-3])

print(list2)

print("*" * 50)
# list1 = list(1, 2, 3, 4, 5)
# print(list1)

list1 = list((1, 2, 3, 4, 5))
print(list1)

print("*" * 50)

myList = ['abc', 15, 15.5, True, 'test']
print(myList)
# other data type immutable they can not be changed
# list is mutable

myList[1] = 100
# myList[10] = 100
print(myList)

print(len(myList))

print("*" * 50)

myList.append('new_item')
print(myList)

print("*" * 50)
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list2[5])
x = list2[5]
print(x)
print(list2[:])
print(list2[3:])
print(list2[3:8])
print(list2[0:8])
print(list2[0:8: 2])
x = list2[0:8: 2]
print(x)
print(list2[::-1])
print(list2[-1:-11:-1])
print(list2[-1:-11:-2])

print(list2[0:3])
print("*" * 50)
list2[0:3]=[10, 20, 30]
print(list2)

list2[0:3]=[11, 12]
print(list2)

list2[0:3]=[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(list2)

print("*" * 50)
print(list2[::4])
list2[::4] = [21, 22, 23, 24]
print(list2)

print("*" * 50)

list3 = [1, 2, 3]
list4 = [4, 5, 6]
print(list3 + list4 + [7, 8, 9])

print("*" * 50)
list3.extend([4, 5])
print(list3)

print("*" * 50)

list3 = list3 + [11, 15]
print(list3)

print("*" * 50)

list5 = [1, 2, 3]
print(list5 * 3)

print(1 in list5)
print(5 in list5)
print(5 not in list5)

if 3 in list5:
    print("3 is in list5")
else:
    print("3 is not in list5")