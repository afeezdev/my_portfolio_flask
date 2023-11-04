from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_work():
    return render_template('./index.html')

@app.route('/blog')
def blog():
    return render_template('./index2.html')

@app.route('/blog/2022/dog')
def blog2():
    return 'This is my dog'

