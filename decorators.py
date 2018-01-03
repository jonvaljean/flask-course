#a decorator is a function that gets called before another function
#SAVE THESE TEMPLATES for decorators with and without parameters

import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("in the decorator!")
        func()   #always call the function inside the decorator or it will not work
        print("after the decorator!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm the function !")

my_function()

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator !")
            if number == 56:
                print("Not running the function !")
            else:
                func(*args, **kwargs)
            print("After the decorator !")
        return function_that_runs_func
    return my_decorator




@decorator_with_arguments(57)
def my_function_too(x,y):
    print("Hello", x + y)

my_function_too(57,67)
