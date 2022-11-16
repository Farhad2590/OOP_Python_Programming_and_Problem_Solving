numbers = [12,45,40,54,56,58,60,62]
# print(numbers[1])
# print(numbers[-4])
#Slice = list [start : end : step]
# print(numbers[1:6])
# print(numbers[2 : 8 : 2])
# print(numbers[2 : 8 : 2])
# print(numbers[5:2:-1])
# print(numbers[:])
# print(numbers[: :])

#Sort the items of the list in place 
numbers.sort()
# print(numbers)

#Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
numbers.remove(45)
# print(numbers)

numbers.reverse()
# print(numbers)

#Add an item to the end of the list. Equivalent to a[len(a):] = [x].
numbers.append(94)
# print(numbers)

numbers.insert(3, 45)
# print(numbers)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
print(fruits)

fruits.count('tangerine')
print(fruits)

fruits.index('banana')
print(fruits)

fruits.index('banana', 4)  # Find next banana starting at position 4
print(fruits)

fruits.reverse()
print(fruits)

['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits)

['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'