a = ['oh', 'Emelia', 'to']
s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
def create_new_string(s):
    s = s.replace(',', "")
    s = s.replace('.', "")
    splited_string = s.split()

    words = [splited_string[i + 1] for i in range(
        len(splited_string)) if splited_string[i].lower() in a or splited_string[i] in a]

    # print (words)
    return "".join([" " + i for i in words])[1:]


output = create_new_string(s)

with open('out.txt', 'w') as fileWriter:
    fileWriter.write(output)