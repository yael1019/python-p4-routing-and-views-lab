#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str>')
def print_string(str):
    print(str)
    return str

@app.route('/count/<int:num>')
def count(num):
    count = f''
    for n in range(num):
        count += f'{n}'
    return range(count)

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+': return num1 + num2
    elif operation == '-': return num1 - num2
    elif operation == '*': return num1 * num2
    elif operation == 'div': return num1 / num2
    elif operation == '%': return num1 % num2

if __name__ == '__main__':
    app.run(port=5555, debug=True)
