from flask import Flask
from flask import render_template, request, redirect
import data
import bcrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()

# put your code here