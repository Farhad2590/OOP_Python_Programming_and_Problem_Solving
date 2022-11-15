try:
    num = 15/0
    print(num)
except:
    print('Something Went wrong')
finally:
    print('This is Done')

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

try:
    if '1' != 1:
        raise "someError"
    else:
        print("someError has not occurred")
except:
    print ("someError has occurred")