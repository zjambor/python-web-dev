from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# SET FLASK_APP=hello_flask.py
# flask run

# add variable to url
@app.route('/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/<name>/<int:number>')
def greet_with_years(name, number):
    return f'Hello, {name}, you are {number} years old!'

if __name__ == "__main__":
    app.run(debug=True)
