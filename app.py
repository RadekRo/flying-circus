from flask import Flask, session
from flask import render_template, request, redirect
import bcrypt, data_handler

app = Flask(__name__)
app.secret_key = bcrypt.gensalt()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        user_data = data_handler.get_user_data(login)
        if user_data == None or data_handler.check_password(user_data, password) == False:
            return render_template("login.html", error = 'Wrong user name or password')
        else:
            session['username'] = login
            return render_template('index.html', message = 'Logged in!')

@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        password = request.form.get('password')
        password_repeat = request.form.get('password-repeat')
        if data_handler.check_password_repeat(password, password_repeat) == False:
            return render_template('signin.html', error = 'wrong-login-repeat')
        else:
            login = request.form.get('login')
            hashed_password = data_handler.hash_password(password)
            data_handler.add_new_user(login, hashed_password)
            return render_template('login.html', message = 'Sign in completed, you can log in now!')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        if 'username' in session:
            
            if 'current_question' in session:
                session['current_question'] += 1
            else:
                session['current_question'] = 0
            
            question = data_handler.get_current_question(session['current_question'])
            answers = data_handler.get_current_answers(question)
            return render_template('test.html', question = question, answers = answers)
        else:
            return redirect('/')
    else:
        pass

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run()

# put your code here