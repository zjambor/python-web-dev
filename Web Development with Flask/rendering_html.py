from flask import Flask

app = Flask(__name__)

# Decorator functions
def make_bold(fn):
    def wrapper():
        return f'<b>{fn()}</b>'
    return wrapper

def make_emphasis(fn):
    def wrapper():
        return f'<em>{fn()}</em>'
    return wrapper

def make_underlined(fn):
    def wrapper():
        return f'<u>{fn()}</u>'
    return wrapper

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragraph</p>' \
    '<img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Cute_grey_kitten.jpg" width=300>'

# add variable to url
@app.route('/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/<name>/<int:number>')
def greet_with_years(name, number):
    return f'Hello, {name}, you are {number} years old!'

if __name__ == "__main__":
    app.run(debug=True)
