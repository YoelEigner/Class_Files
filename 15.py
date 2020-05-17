from gc import collect
def addition(a, b):
    result = a + b
    print(result)


def subs(a, b):
    print("subs")

subs(2, 4)
subs(3, 5)
addition(8, 15)



collect()