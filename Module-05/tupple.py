numbers = [12,45,40,54,56,58,60,62]
print(numbers)
numbers_tupple = 12,45,40,54,56,58,60,62
print(numbers_tupple)
print(numbers_tupple[0])
nums = (12,45,56)
print(nums)
#'tuple' object does not support item assignment

tuple2D = ([12,54,90],[45,11.20])
tuple2D[0][1] =99
tuple2D[1][1] =99
print(tuple2D)

tuple_from_list = tuple(numbers)
print(tuple_from_list)