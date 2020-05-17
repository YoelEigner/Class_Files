from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        return '<font size=7>My name is Toaster</font>'
    elif request.method == 'POST':
        return 'creating your name'


app.run(host="localhost", port=5001, debug=True)
