from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to home page"


@app.route('/city')
def city():
    return "Welcome to bangalore"


@app.route('/org')
def org():
    return "Welcome to RNTBCI"


if __name__ == '__main__':
    app.run(debug=True)
