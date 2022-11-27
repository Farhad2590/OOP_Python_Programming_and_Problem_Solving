# def do_something(X,Y):
#     print(f'X: {X} Y: {Y}')

# do_something (12,45)
# do_something ('Tomatto','Onion')
def do_something(Work):
    print("Start The Work")
    # print(Work)
    # print(type(Work))
    Work()
    print("Finished Work")
def Practice_coding():
    print("I am Practacing Coding")

def Leraning_python():
    print("I am learning python")

do_something(Practice_coding)
do_something(Leraning_python)