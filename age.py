def get_age():
    user_age = int(input("Please enter your age"))
    if user_age < 0:
        raise ValueError("Age cannot be negative")

try:
    get_age()
except ValueError as e:
    print("Failed because " + str(e))