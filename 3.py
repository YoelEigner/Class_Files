first = 7
second = 44.3
print(first + second)
print(first * second)
print(second / first)

a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8

print(a, b, c)
# a = 9, b = 8, c = 15

# use single quotes if you want to use double quote in string
name = "John"
name = 'John'
print(name)

# Python is unable to concatenate a string and int
my_number = 5 + 5
print("Result is: " + str(my_number))

# output is 7
x = 5
y = 2.36
print(x + int(y))


a = 8
b = "123"
print("%d" % a + b)
print(f"{a}{b}")
