def clean_string(output):
    output = ''.join(i for i in output if i.isspace() or i.isalpha())
    print(output)
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)

