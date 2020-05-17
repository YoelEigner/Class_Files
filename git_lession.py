def my_wrapper(to_print):
    print("---------------")
    print(to_print)
    print("----------------")


input_from_user = input("Enter your name: ")
age = int(input("Enter your age: "))
my_wrapper("Your name is: " + input_from_user + " " + str(age))
