def names():
    get_name = input("Please enter your name: ")
    name = open("names.txt", "a")
    name.write(get_name + "\n")
    name.close()
    return name


def print_names():
    name_txt = open("names.txt")
    for name in name_txt.readlines():
        print("Hello mr. " + name, end='')


for i in range(10):
    names()
print_names()