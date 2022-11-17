# looping in list
numbers = [12,45,40,54,56,58,60,62]

# total = sum(numbers)
# print(total)

total = 0
for i in numbers:
    total += i
    # print(i)
# print(total)

# looping in set
numbers = {12,40,40,54,56,54,60,62}

total = 0
for i in numbers:
    total += i
#     print(i)
# print(total)
# looping in tupple
numbers_tupple = 12,45,40,54,56,58,60,62
total = 0
for i in numbers_tupple:
    total += i
    # print(i)
# print(total)

# looping in dictionary
marks = { 'physics': 21, 'chemistry ':  45, 'math': 56 }
for mark in marks:
    val = marks[mark]
    # print(mark,val)

# for subject, mark in marks.items():
    # print(subject,marks

for i, num in enumerate(numbers):
    print(i,num)