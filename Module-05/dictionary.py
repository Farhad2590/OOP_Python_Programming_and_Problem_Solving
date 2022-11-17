marks = { 'physics': 21, 'chemistry ':  45, 'math': 56 }
marks['math'] = 56.5
marks['English'] = 89
del marks['chemistry ' ]
print (marks)
#find keys

marks_keys = marks.keys()
print(marks_keys)

marks_values = marks.values()
print(marks_values)

marks_items = marks.items()
print(marks_items)