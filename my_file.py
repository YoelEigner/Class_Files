a = int(input("enter first number: "))
b = int(input("enter second number: "))

try:
    open("asdasdas")
except BaseException as e:
    print(e.args)
