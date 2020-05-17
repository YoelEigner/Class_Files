import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='8323eigneR', db='yoel', autocommit=True)

cursor1 = connection.cursor()

cursor1.execute("select * from students")

for row in cursor1:
    print(row)

# cursor1.execute("insert into students values ('741258963', 'Toaster', 'Eigner', 3)")
cursor1.execute("update students set age ='63' where id = '123123123'")


