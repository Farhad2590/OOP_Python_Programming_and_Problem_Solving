""" cht bot

steps :
1.input
2.decide
3.output
"""
greet_words = ['hi','hello','yo']
bye_words = ['bye','tata', 'hasta la vista']
bad_words = ['d0g','pocha']
def listen():
    return input('say something: ')
def decide(comand):
    # print(comand)
    comand = comand.lower()
    broken_words = comand.split()

    for word in broken_words:
        if word in greet_words:
            talkback('ki obosta man')
            break
        elif word in bye_words:
            talkback('Tata See you again')
            break
        elif word in bad_words:
            talkback('you using slang world . plz behave your self')
            break
def talkback(response):
    print(response)

while True:
    comand = listen()
    decide(comand)
