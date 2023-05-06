from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        pass

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "GET":
        return render_template("sign-in.html")
    else:
        login = request.form.get('login')
        login_repeat = request.form.get('login-repeat')
        if login != login_repeat:
            return render_template("sign-in.html", error = "wrong-login-repeat")

if __name__ == '__main__':
    app.run()

# put your code here