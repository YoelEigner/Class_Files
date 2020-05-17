isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
names = ["David", "Haim", "John", "Avner"]
my_name = "David"
names = ["Yoel", "David", "Yoel"]
if names.__contains__(my_name):
    print("My name is in the list")
else:
    print("My name is not in the list")
if my_name in ["David", "Haim", "John", "Avner"]:
    print("Your name is in the list as well")

if names:
    print("There are names")
else:
    print("No Names")


if len(names) < 3:
    print("We have no names")
elif len(names) > 3:
    print("We have names")


x = 5
y = 5
if type(x) is int:
    print(type(x))

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

