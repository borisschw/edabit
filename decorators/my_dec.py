import math
import time

def get_execution_time(func):
    def get_time(*args, **kw):

        startTime = time.time()
        func_result = func(*args,**kw)
        endTime = time.time()
        print("Total function {} time is {}".format(func.__name__, endTime - startTime))
        return func_result
    return get_time



@get_execution_time
def my_factorial(num):
    res = math.factorial(num)
    time.sleep(0.1)
    return res




# Python program to illustrate functions
# Functions can return another function

def create_adder(x):

    def adder(y):
        print(y)
        return x+y
    print(x)
    return adder

add_15 = create_adder(15)
print(add_15(10))








