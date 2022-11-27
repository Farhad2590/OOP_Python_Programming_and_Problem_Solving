import math
import time
def timer(func):
    def inner(*args, **kwargs):
        print("Time Start")
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f"Time End. Total time taken{end - start}")
    return inner
@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is: {result}")

get_factorial(n = 100)