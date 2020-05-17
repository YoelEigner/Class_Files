import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='8323eigneR', db='yoel', autocommit=True)

cursor1 = connection.cursor()


def new_animal(cursor_to_execute):
    name_of_animal = input("enter animal name: ")
    type_of_animal = input("enter animal type: ")
    age_of_animal = int(input("enter animal age: "))
    cursor_to_execute.execute(f"insert into animals values ('{name_of_animal}','{type_of_animal}',{age_of_animal})")


def new_animal(cursor_to_execute):
    name_of_animal = input("enter animal name: ")
    type_of_animal = input("enter animal type: ")
    age_of_animal = int(input("enter animal age: "))
    cursor_to_execute.execute(f"insert into animals values ('{name_of_animal}','{type_of_animal}',{age_of_animal})")


def delete_animal(cursor_to_execute, animal_name):
    cursor_to_execute.execute(f"delete from dogs where name = '{animal_name}'")


# new_animal(cursor1)

def show_animals(cursor_to_execute):
    cursor_to_execute.execute("select * from animals")
    for row in cursor_to_execute:
        print(f"name is {row[0]}, age is: {row[2]}, type: {row[1]}")

delete_animal(cursor1, 'Balu')
# new_animal(cursor1)
# new_animal(cursor1)
# show_animals(cursor1)
