my_global_varb = 5
def my_own_printer(to_print):
    print("---------------")
    print(to_print)
    print("----------------")

input_from_user = input("Enter your name: ")
age = int(input("Enter your age: "))
my_own_printer("Your name is: " + input_from_user + " " + str(age))
