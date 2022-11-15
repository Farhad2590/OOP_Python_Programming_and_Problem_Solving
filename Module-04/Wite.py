# with open ('Message.txt','a') as fileWrite:
#     fileWrite.write('Again Hello From Python')
with open('Message.txt','r') as fileRead:
    text = fileRead.read()
    print(text)