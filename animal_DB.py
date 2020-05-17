from flask import Flask, redirect, request, render_template
import pymysql

app = Flask(__name__)

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='8323eigneR', db='yoel', autocommit=True)

cursor1 = connection.cursor()


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/showdogs', methods=['GET'])
def show_animals():
    cursor1.execute("select * from dogs")
    values = cursor1.fetchall()
    return render_template("show_dogs.html", value=values)

    # for dog in values:
    #     return str(dog[1])


@app.route('/', methods=['POST'])
def dogs():
    name = request.form['name']
    age = int(request.form['age'])
    breed = request.form['breed']
    cursor1.execute(
        f"insert into dogs values ('{name}',{age},'{breed}')")
    return redirect('/showdogs')


app.run(host="localhost", port=5001, debug=True)
