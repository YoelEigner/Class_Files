from  datetime import datetime
from time import sleep


def my_decorator(func):
    def wrapper():
        print(datetime.now())
        func()
        print(datetime.now())

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


say_whee()