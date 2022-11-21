def test_script():
    make_upper(str)
    make_capital(str)
    make_lower(str)

def make_upper(str):
    output = ""
    for i in str:
        if ord(i) >= 97 and ord(i)<=120:
            output+=chr(ord(i)-32)
    return output

def make_lower(str):
    output = ""
    for i in str:
        if ord(i) >= 65 and ord(i)<=90:
            output+=chr(ord(i)+32)
    return output

def make_capital(str):
    output = ""
    if ord(str[0]>=97) and ord(str[0])<=120:
        letter = ord(str[0])-32
    return output

if __name__ == "main":
    res = test_script(str)
    print(res)