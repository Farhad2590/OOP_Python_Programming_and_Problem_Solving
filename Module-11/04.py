from unittest import result


input_ = "x3b4U5i2"

result_list = [input_[i]*int(input_[i+1]) for i in range(0, len(input_), 2)]
result_list.sort(key=str.lower)
result = ''.join(result_list)
print(result)