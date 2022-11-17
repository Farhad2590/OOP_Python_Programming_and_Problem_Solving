numbers = [12,45,40,54,56,58,60,62]

odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)
# print(odd_numbers)

odd_numbers2 = [num * 2 for num in numbers if num %2==1]
print(odd_numbers2)