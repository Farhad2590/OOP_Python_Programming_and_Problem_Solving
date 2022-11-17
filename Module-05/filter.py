numbers = [12,45,40,54,56,58,60,62]

bigger_numbers = filter(lambda x : x > 50,numbers)
# print(numbers)
# print(list(bigger_numbers))

user = [{'name' : 'sakib','age':34},
{'name' : 'savana','age':36},
{'name' : 'sanjida','age':33},
{'name' : 'sazzad','age':45},
{'name' : 'sadia','age':25}]


senior = filter(lambda actor : actor['age'] > 35,user)
junior = filter(lambda actor : actor['age'] < 35,user)
print(list(junior))
print(list(senior))