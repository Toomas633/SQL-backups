from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = '$2b$12$R0hxaE9n7B.r5ls7UnFBC.tLtsO0h/CrhYyW4kLdeyR5XhTI11Pv.'
bcrypt = Bcrypt(app)

# Simulated user data (replace this with a proper user database)
users = {'admin': '$2b$12$tHpzFajntiEAF.u8qIPyd.1Wx2.37.gf1TReAOVPLUfRUIj5WnIlK'}


@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and bcrypt.check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return f"Welcome to your dashboard, {username}!"
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
