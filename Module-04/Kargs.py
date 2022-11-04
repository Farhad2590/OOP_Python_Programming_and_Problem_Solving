def add(num1,*numbers):
    print(num1)
    print(numbers)

add(3,4,5,6,7)

def full_name(f_name, l_name):
    name = f'{f_name} {l_name}'
    return name

name = full_name(l_name = 'chowdhury',f_name= 'farhad')
print(name)

def long_name(**kargs):
    print(kargs)

long_name(first = 'Dr', last = 'Farhad', midle = 'Hossen')

def name_mixed(first,last, **name_parts):
    print(first,last,name_parts)

name = name_mixed(first = 'chowdhury',last= 'farhad',middle='Dr',Majari = 'Hosse')
print(name)

def all_types(first,*args,**kargs):
    print(first)
    print(args)
    print(kargs)

all_types('adb', 'ddds', 'sghh', 'aghjs',name = 'abul', father = 'babul')


def all_types(first,*args,**kargs):
    print(first)
    for word in args:
         print(word)
    for key,value in kargs.items():
        print(key, value)
all_types('adb', 'ddds', 'sghh', 'aghjs',name = 'abul', father = 'babul')