import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator
def f1():
    print("This is function")

f1()