numbers = [12,40,45,56,55,61,20,14,62]
# numbers = {12,40,40,54,56,54,60,62}
max_numbers = max(numbers)
print(max_numbers)

min_numbers = min(numbers)
print(min_numbers)

numbers_reverse = reversed(numbers)
print(list(numbers_reverse))

sorted_numbers = sorted(numbers)
print(sorted_numbers)
sorted1_numbers = sorted(numbers, reverse=True)
print(sorted1_numbers)

actors = [{'name' : 'Salman Khan', 'age' : 54},
          {'name' : 'Sakib Khan', 'age' : 32},
          {'name' : 'Sahrukh Khan', 'age' : 51},
          {'name' : 'Sahid Khan', 'age' : 34},
          {'name' : 'Jahid Khan', 'age' : 38},
          {'name' : 'Amir Khan', 'age' : 44}

]

sorted_actors = sorted(actors, key= lambda actor: actor['age'])
print(sorted_actors)