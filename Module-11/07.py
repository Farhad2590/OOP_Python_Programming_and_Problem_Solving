def subset(set, index):
    if index == len(set): return [[]]
    return subset(set, index+1)+[[set[index]] + x for x in subset(set, index+1)]

Input = [4, 5, 6]
Output = subset(Input, 0)
print(Output)