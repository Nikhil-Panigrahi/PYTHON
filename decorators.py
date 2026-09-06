# a decorator is a function that takes a function as a parameter wraps the function and the inner function and performs the job it has to do and returns the inner function
# A decorator is a function that takes another function as input, adds some extra behavior around it, and returns a new function.

def logtime(func):
    def wrapper():
        print("before")
        # do something
        func()
        # do something after
        print("after")
       
    return wrapper 

@logtime # if we remove the @logtime the hello() function wll only print Hello!

def hello():
    print("Hello!")

hello()

# if we do not want to use the shortcut ie @ we can also do the below

decorated_func = logtime(hello)
decorated_func()