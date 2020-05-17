import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='8323eigneR', db='yoel', autocommit=True)

cursor1 = connection.cursor()


def new_animal(cursor_to_execute):
    name = input("enter animal name: ")
    age = int(input("enter animal age: "))
    breed = input("enter animal breed: ")
    cursor_to_execute.execute(f"insert into dogs values ('{name}',{age},'{breed}')")


def show_animals(cursor_to_execute):
    cursor_to_execute.execute("select * from dogs")
    for row in cursor_to_execute:
        print(f"name is {row[0]}, age is: {row[2]}, breed: {row[1]}")


new_animal(cursor1)
