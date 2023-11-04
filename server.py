from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_work():
    return 'Hello, Afeez!, How '

@app.route('/blog')
def blog():
    return 'Hello, these are my thoughts on blogs'

@app.route('/blog/2022/dog')
def blog2():
    return 'This is my dog'

a = 2
a = 3
print(a)