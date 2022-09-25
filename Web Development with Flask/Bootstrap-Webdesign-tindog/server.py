from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/progress-bar')
def progressbar():
    return render_template("progress-bar.html")

@app.route('/containers')
def containers():
    return render_template("containers.html")

@app.route('/carousel')
def carousel():
    return render_template("carousel.html")

if __name__ == "__main__":
    app.run(debug=True)
