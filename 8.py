# A
x = 3
y = 2
if x > y:
    print("Big")
elif x < y:
    print("Small")

# B
for num in range(5):
    print(num)

# C
number = 3
if number == 1:
    print("Summer")
elif number == 2:
    print("Winter")
elif number == 3:
    print("fall")
elif number == 4:
    print("Spring")

# D
##       loop will run 10 times Last nuumber will be 10

# E
my_array = [24, "E", "ILS", "False", 5]
for i in my_array:
    print(i)
print(my_array[1] + my_array[2])

# F
phone_number = input("Enter yur phone number")
print("Your phone number is: " + phone_number)


# G
def printHello():
    print("Hello")


def calculate():
    print(5 + 3.2)


# H
def yourName(name):
    print(name)

#I
def calc(x):
    return x / 2


# J
def multiCalc(x, y):
    return x + y


def add_strings(x, y):
    return x + " " + y


#K
def hastag(x):
    rng = range(x)
    for i in rng:
        print("X" * i)

hastag(7)

i = 0
j = 6
for row in range(7):
    for col in range(7):
        if row == i and col == j:
            print("#", end="")
            i = i + 1
            j = j - 1
        elif row == col:
            print("#", end="")
        else:
            print(end=" ")
    print()
