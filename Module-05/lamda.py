# https://docs.python.org/3/library/functions.html#map
# def square(x):
#     return x *x

# result = square(6)
# print (result)

square = lambda x:x*x

result = square(6)
# print(result)

add = lambda x, y : x + y
sum = add(45,56)
# print(sum)

numbers = [12,45,40,54,56,58,60,62]

def double_it(x):
    return x * 2
double_it2 = lambda x : x * 2 
# doubled_numbers = map(double_it, numbers)
doubled_numbers = map(lambda x : x * 2,numbers)
squared_numbers = map(lambda x : x * x,numbers)
print(numbers)
print(list(doubled_numbers))
print(list(squared_numbers))


